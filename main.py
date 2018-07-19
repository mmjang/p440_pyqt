import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import Qt, QtCore
from main_window import Ui_MainWindow
import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt
import utils
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import threading
from scipy.signal import hilbert, chirp
import socket
from struct import *
from threading import Thread, Condition, Lock
import p440_config

queue = []
lock = Lock()
count = 200

ip = '192.168.1.100'
port = 21210

'''
message_type    uint16
message_id      uint16
node_id         uint32
scan_start      int32
scan_end        int32
scan_resolution uint16
base_int_index  uint16
seg1            uint16
seg2            uint16
seg3            uint16
seg4            uint16
seg1_int        uint8
seg2_int        uint8
seg3_int        uint8
seg4_int        uint8
antenna_mode    uint8
transmit_gain   uint8
code_channel    uint8
persist_flag    uint8
'''

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_callback()
        # self.set_up_ports()
        # self.set_up_gains()
        self.showFullScreen()
        self.show()

        # #set signal
        # self.ui.com_btn.clicked.connect(self.com_btn_clicked)
        # #global variables
        # self.gain_map = None
        # self.serial_port = None

        #setup matplotlib
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.ui.figure_layout.addWidget(self.toolbar)
        self.ui.figure_layout.addWidget(self.canvas)
        self.ax1 = self.figure.add_subplot(111)
        #ax1.plot(np.sin(np.arange(1,100,0.1)))
        #ax2 = self.figure.add_subplot(212)
        #ax2.plot(np.cos(np.arange(1,100,0.1)))       
        plt.tight_layout()
        self.canvas.draw()

        #setup timer
        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.update_canvas)
        # timer.start(300)

        # self.producer = ProducerThread().start()

        self.data_arr = []
        self.iter = 0
    
    def set_callback(self):
        self.ui.btn_read_config.clicked.connect(self.read_config)
        self.ui.btn_close.mouseReleaseEvent = lambda self, event: app.quit()

        self.ui.btn_0.clicked.connect(lambda x:self.write_number(0))
        self.ui.btn_1.clicked.connect(lambda x:self.write_number(1))
        self.ui.btn_2.clicked.connect(lambda x:self.write_number(2))
        self.ui.btn_3.clicked.connect(lambda x:self.write_number(3))
        self.ui.btn_4.clicked.connect(lambda x:self.write_number(4))
        self.ui.btn_5.clicked.connect(lambda x:self.write_number(5))
        self.ui.btn_6.clicked.connect(lambda x:self.write_number(6))
        self.ui.btn_7.clicked.connect(lambda x:self.write_number(7))
        self.ui.btn_8.clicked.connect(lambda x:self.write_number(8))
        self.ui.btn_9.clicked.connect(lambda x:self.write_number(9))
        self.ui.btn_dot.clicked.connect(lambda x:self.write_number(-1))
        self.ui.btn_del.clicked.connect(lambda x:self.write_number(-2))

    def read_config(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #set operation mode
        s.sendto(pack('HHI', 0xf003, 0, 1), (ip, port))
        confirm_message, addr = s.recvfrom(1500)
        if confirm_message[0:2] == b'\xf1\x03':
            print('successful')
        else:
            print('error')
            return
        packet_get_config = pack('>HH', 0x1002, 0)
        s.sendto(packet_get_config, (ip, port))
        config_message, addr = s.recvfrom(1500)
        self.current_config = p440_config.Config(config_message)
        pass

    def update_canvas(self):
        global queue
        if queue:
            lock.acquire()
            if len(self.data_arr) == 0:
                self.data_arr = np.zeros((count, len(queue[0])))
            self.ax1.clear()
            for line in queue:
                self.data_arr[self.iter] = line
                self.iter += 1
                print(self.iter)
            envelop = np.abs(hilbert(self.data_arr[0:-1] - self.data_arr[1:]))
            if self.iter - 1 < len(envelop):
                envelop[self.iter - 1] = 0
            
            for line in envelop:
                line = np.clip(np.round(63 * line / 10e3) + 1, -1e5, 64)
            self.ax1.imshow(envelop[0:-1], aspect = 'auto')
            self.canvas.draw()
            queue = []
            lock.release()

    def write_number(self, number):
        '''
            0 - 9
            -1 for '.'
            -2 for backsapce
        '''
        all_line_edits = [
            self.ui.lineEdit_distance_start,
            self.ui.lineEdit_distance_end,
            self.ui.lineEdit_interval,
            self.ui.lineEdit_integration_index,
            self.ui.lineEdit_gain
        ]
        for edit in all_line_edits:
            if edit.hasFocus():
                focused = edit
                break
        
        if not focused:
            return 

        if number <= 9 and number >= 0:
            input_char = str(number)

        elif number == -1:
            input_char = '.'

        current_text = focused.text()
        
        if number == -2:
            if current_text:
                current_text = current_text[0:-1]
        
        else:
            current_text = current_text + input_char
        
        edit.setText(current_text)

        


    # def set_up_ports(self):
    #     ports = list(serial.tools.list_ports.comports())
    #     for port in ports:
    #         self.ui.com_selector.addItem(port[0])

    # def set_up_gains(self):
    #     self.gain_map = {}
    #     gain_list = utils.load_gain_data()
    #     for item in gain_list:
    #         self.ui.gain_selector.addItem(item[0])
    #         self.gain_map[item[0]] = item[1]
    
    #callbacks
    # def com_btn_clicked(self, e):
    #     if (not self.serial_port) or (not self.serial_port.isOpen()):
    #         index_com = self.ui.com_selector.currentIndex()
    #         index_baud = self.ui.baud_selector.currentIndex()
    #         com = self.ui.com_selector.itemText(index_com)
    #         baud = self.ui.baud_selector.itemText(index_baud)
    #         #try:
    #         self.serial_port = serial.Serial(com)
    #         self.serial_port.baudrate = int(baud)
    #         self.ui.com_btn.setStyleSheet('background-color:green;color:white;')
    #         self.ui.com_btn.setText('关闭串口')
    #         #except:
    #             #QMessageBox.about(self, 'Warning', 'Failed to open port!')
    #         self.StartThread()
    #     else:
    #         if self.serial_port.isOpen():
    #             self.StopThread()
    #             self.serial_port.close()
    #         self.ui.com_btn.setStyleSheet('color:black;')
    #         self.ui.com_btn.setText('打开串口')

class ProducerThread(Thread):
    def run(self):
        ip = '192.168.1.100'
        port = 21210

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.settimeout(1.0)
        #s.connect((ip, port))
        count = 200
        packet_get_config = pack('>HHHHI', 0x1003, 0, count, 0, 150 * 1000)
        s.sendto(packet_get_config, (ip, port))

        #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s1.bind((ip, port))
        start_of_number_of_samples = 2 * 2 + 4 * 6 + 4 * 2 + 2 + 4

        dt = np.dtype(int)
        dt = dt.newbyteorder('>')
        global queue

        i = 0
        while True:
            data, addr = s.recvfrom(1500)
            #print('received' + str(len(data)))
            #print(data[0:2])
            #print(data, addr)
            if data[0:2] == b'\xf2\x01':
                #print(len(data))
                this_len, total_len, this_index, total_index = unpack('>HIHH', data[start_of_number_of_samples:start_of_number_of_samples + 10])
                if this_index == 0:
                    binary_buff = b''
                temp = data[start_of_number_of_samples + 10: start_of_number_of_samples + 10 + this_len * 4]
                binary_buff = binary_buff + temp
                if this_index == total_index - 1:
                    print('binarybuff ' + str(i))
                    i += 1
                    #print(binary_buff)
                    new_signal = np.frombuffer(binary_buff, dtype = dt)
                    lock.acquire()
                    queue.append(new_signal)
                    lock.release()
                    if i == count:
                        break

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
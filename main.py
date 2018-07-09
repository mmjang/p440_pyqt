import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from PyQt5 import Qt
from main_window import Ui_MainWindow
import serial
import serial.tools.list_ports
import numpy as np
import matplotlib.pyplot as plt
import utils
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import threading

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_up_ports()
        self.set_up_gains()
        self.show()

        #set signal
        self.ui.com_btn.clicked.connect(self.com_btn_clicked)
        #global variables
        self.gain_map = None
        self.serial_port = None
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.alive = threading.Event()

        self.ui.figure_layout.addWidget(self.toolbar)
        self.ui.figure_layout.addWidget(self.canvas)
        #ax1 = self.figure.add_subplot(211)
        #ax1.plot(np.sin(np.arange(1,100,0.1)))
        #ax2 = self.figure.add_subplot(212)
        #ax2.plot(np.cos(np.arange(1,100,0.1)))       
        #plt.tight_layout()
        #self.canvas.draw()

    def set_up_ports(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            self.ui.com_selector.addItem(port[0])

    def set_up_gains(self):
        self.gain_map = {}
        gain_list = utils.load_gain_data()
        for item in gain_list:
            self.ui.gain_selector.addItem(item[0])
            self.gain_map[item[0]] = item[1]
    
    #callbacks
    def com_btn_clicked(self, e):
        if (not self.serial_port) or (not self.serial_port.isOpen()):
            index_com = self.ui.com_selector.currentIndex()
            index_baud = self.ui.baud_selector.currentIndex()
            com = self.ui.com_selector.itemText(index_com)
            baud = self.ui.baud_selector.itemText(index_baud)
            #try:
            self.serial_port = serial.Serial(com)
            self.serial_port.baudrate = int(baud)
            self.ui.com_btn.setStyleSheet('background-color:green;color:white;')
            self.ui.com_btn.setText('关闭串口')
            #except:
                #QMessageBox.about(self, 'Warning', 'Failed to open port!')
            self.StartThread()
        else:
            if self.serial_port.isOpen():
                self.StopThread()
                self.serial_port.close()
            self.ui.com_btn.setStyleSheet('color:black;')
            self.ui.com_btn.setText('打开串口')

    #Threading
    def StartThread(self):
        self.thread = threading.Thread(target=self.PortThread)
        self.thread.setDaemon(1)
        self.alive.set()
        self.thread.start()

    def StopThread(self):
        if self.thread:
            self.alive.clear()
            self.thread.join()
            self.thread = None
                
    def PortThread(self):
        while self.alive.is_set() and self.serial_port.isOpen():
            self.ui.com_btn.setText('yes')    
            #print('alive')
            if self.serial_port.inWaiting() > 0:
                #print('inWaiting')
                data_str = self.serial_port.read(self.serial_port.inWaiting())
                #self.serial_port.write(data_str)
                self.ui.com_btn.setText(str(data_str.decode('ascii') + '\n'))

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
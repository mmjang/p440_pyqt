# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_1 = QtWidgets.QPushButton(self.tab)
        self.btn_1.setGeometry(QtCore.QRect(450, 70, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_1.setFont(font)
        self.btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.tab)
        self.btn_2.setGeometry(QtCore.QRect(550, 70, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_2.setFont(font)
        self.btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.tab)
        self.btn_3.setGeometry(QtCore.QRect(650, 70, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_3.setFont(font)
        self.btn_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.tab)
        self.btn_4.setGeometry(QtCore.QRect(450, 160, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_4.setFont(font)
        self.btn_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.tab)
        self.btn_5.setGeometry(QtCore.QRect(550, 160, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_5.setFont(font)
        self.btn_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.tab)
        self.btn_6.setGeometry(QtCore.QRect(650, 160, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_6.setFont(font)
        self.btn_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.tab)
        self.btn_7.setGeometry(QtCore.QRect(450, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_7.setFont(font)
        self.btn_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.tab)
        self.btn_8.setGeometry(QtCore.QRect(550, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_8.setFont(font)
        self.btn_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.tab)
        self.btn_9.setGeometry(QtCore.QRect(650, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_9.setFont(font)
        self.btn_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_9.setObjectName("btn_9")
        self.btn_0 = QtWidgets.QPushButton(self.tab)
        self.btn_0.setGeometry(QtCore.QRect(550, 340, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_0.setFont(font)
        self.btn_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_0.setObjectName("btn_0")
        self.btn_dot = QtWidgets.QPushButton(self.tab)
        self.btn_dot.setGeometry(QtCore.QRect(450, 340, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_dot.setFont(font)
        self.btn_dot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_dot.setObjectName("btn_dot")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 100, 401, 42))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_distance_start = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_distance_start.setFont(font)
        self.lineEdit_distance_start.setObjectName("lineEdit_distance_start")
        self.horizontalLayout.addWidget(self.lineEdit_distance_start)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_distance_end = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_distance_end.setObjectName("lineEdit_distance_end")
        self.horizontalLayout.addWidget(self.lineEdit_distance_end)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 160, 401, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_interval = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_interval.setFont(font)
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.horizontalLayout_2.addWidget(self.lineEdit_interval)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 220, 401, 42))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_integration_index = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_integration_index.setFont(font)
        self.lineEdit_integration_index.setObjectName("lineEdit_integration_index")
        self.horizontalLayout_3.addWidget(self.lineEdit_integration_index)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 280, 401, 42))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_gain = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_gain.setFont(font)
        self.lineEdit_gain.setObjectName("lineEdit_gain")
        self.horizontalLayout_4.addWidget(self.lineEdit_gain)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.btn_read_config = QtWidgets.QPushButton(self.tab)
        self.btn_read_config.setGeometry(QtCore.QRect(20, 340, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_read_config.setFont(font)
        self.btn_read_config.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_read_config.setObjectName("btn_read_config")
        self.btn_write_config = QtWidgets.QPushButton(self.tab)
        self.btn_write_config.setGeometry(QtCore.QRect(250, 340, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_write_config.setFont(font)
        self.btn_write_config.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_write_config.setObjectName("btn_write_config")
        self.btn_del = QtWidgets.QPushButton(self.tab)
        self.btn_del.setGeometry(QtCore.QRect(650, 340, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_del.setFont(font)
        self.btn_del.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_del.setObjectName("btn_del")
        self.btn_close = QtWidgets.QLabel(self.tab)
        self.btn_close.setGeometry(QtCore.QRect(700, 10, 51, 51))
        self.btn_close.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_close.setText("")
        self.btn_close.setPixmap(QtGui.QPixmap("power_off.png"))
        self.btn_close.setScaledContents(True)
        self.btn_close.setObjectName("btn_close")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 0, 591, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.figure_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.figure_layout.setContentsMargins(0, 0, 0, 0)
        self.figure_layout.setObjectName("figure_layout")
        self.dial = QtWidgets.QDial(self.tab_2)
        self.dial.setGeometry(QtCore.QRect(0, 20, 141, 151))
        self.dial.setObjectName("dial")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "·"))
        self.label.setText(_translate("MainWindow", "范围:"))
        self.label_2.setText(_translate("MainWindow", "—"))
        self.label_3.setText(_translate("MainWindow", "m"))
        self.label_4.setText(_translate("MainWindow", "扫描周期:"))
        self.label_5.setText(_translate("MainWindow", "ms"))
        self.label_6.setText(_translate("MainWindow", "累加次数:2^"))
        self.label_7.setText(_translate("MainWindow", "(6-15)"))
        self.label_8.setText(_translate("MainWindow", "增益:"))
        self.label_9.setText(_translate("MainWindow", "(0-63)"))
        self.btn_read_config.setText(_translate("MainWindow", "读取配置"))
        self.btn_write_config.setText(_translate("MainWindow", "写入配置"))
        self.btn_del.setText(_translate("MainWindow", "del"))
        self.label_10.setText(_translate("MainWindow", "超宽带生命探测仪"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "参数配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "信号处理"))


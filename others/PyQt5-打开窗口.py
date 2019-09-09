#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个代码可以打开一个窗口，上面有“打开”按钮。因为使用pyside2库，所以不用这个代码了
import sys

## 图形化界面 Gui
from PyQt5 import QtCore,QtGui,QtWidgets,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
##

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Gui,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386,127)
        self.centralWidget=QtWidgets.QWidget(MainWindow)
        self.retranslateUi(MainWindow)
        
        self.pushButton=QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190,90,75,23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("打开")
        
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self,MainWindow):
        _translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","窗口"))

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Gui()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

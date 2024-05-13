# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FINAL.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 480)
        MainWindow.setStyleSheet("background-color: rgb(0, 8, 163);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lup = QtWidgets.QPushButton(self.centralwidget)
        self.lup.setGeometry(QtCore.QRect(10, 140, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lup.setFont(font)
        self.lup.setStyleSheet("background-color: rgb(251, 255, 14);")
        self.lup.setObjectName("lup")
        self.ldown = QtWidgets.QPushButton(self.centralwidget)
        self.ldown.setGeometry(QtCore.QRect(10, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ldown.setFont(font)
        self.ldown.setStyleSheet("background-color: rgb(251, 255, 14);")
        self.ldown.setObjectName("ldown")
        self.rup = QtWidgets.QPushButton(self.centralwidget)
        self.rup.setGeometry(QtCore.QRect(500, 140, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rup.setFont(font)
        self.rup.setStyleSheet("background-color: rgb(251, 255, 14);")
        self.rup.setObjectName("rup")
        self.rdown = QtWidgets.QPushButton(self.centralwidget)
        self.rdown.setGeometry(QtCore.QRect(500, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.rdown.setFont(font)
        self.rdown.setStyleSheet("background-color: rgb(251, 255, 14);")
        self.rdown.setObjectName("rdown")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(170, 170, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.left.setFont(font)
        self.left.setStyleSheet("background-color: rgb(126, 243, 76);")
        self.left.setObjectName("left")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(350, 170, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.right.setFont(font)
        self.right.setStyleSheet("background-color: rgb(126, 243, 76);")
        self.right.setObjectName("right")
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(260, 120, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.forward.setFont(font)
        self.forward.setStyleSheet("background-color: rgb(126, 243, 76);\n"
"")
        self.forward.setObjectName("forward")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(260, 220, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(126, 243, 76);")
        self.back.setObjectName("back")
        self.dactance = QtWidgets.QLabel(self.centralwidget)
        self.dactance.setGeometry(QtCore.QRect(130, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dactance.setFont(font)
        self.dactance.setStyleSheet("")
        self.dactance.setObjectName("dactance")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(170, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.one.setFont(font)
        self.one.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(270, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.two.setFont(font)
        self.two.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(370, 340, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.three.setFont(font)
        self.three.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.three.setObjectName("three")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lup.setText(_translate("MainWindow", "L-UP"))
        self.ldown.setText(_translate("MainWindow", "L-DOWN"))
        self.rup.setText(_translate("MainWindow", "R-UP"))
        self.rdown.setText(_translate("MainWindow", "R-DOWN"))
        self.left.setText(_translate("MainWindow", "LEFT"))
        self.right.setText(_translate("MainWindow", "RIGHT"))
        self.forward.setText(_translate("MainWindow", "FORWARD"))
        self.back.setText(_translate("MainWindow", "BACKWORD"))
        self.dactance.setText(_translate("MainWindow", "DISTANCE"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
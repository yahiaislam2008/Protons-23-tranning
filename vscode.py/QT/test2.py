# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 397)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 601, 291))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../Pictures/Saved Pictures/Wallpaper And Links/3- FiewWatch.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.st = QtWidgets.QPushButton(parent=self.centralwidget)
        self.st.setGeometry(QtCore.QRect(14, 310, 251, 41))
        self.st.setObjectName("st")
        self.nd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nd.setGeometry(QtCore.QRect(340, 310, 241, 41))
        self.nd.setObjectName("nd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.st.setText(_translate("MainWindow", "1st"))
        self.nd.setText(_translate("MainWindow", "2nd"))

#     def show1stphoto(self):
#         self.photo.setPixmap(QtGui.QPixmap("C:Users/CAVO TECH/Desktop/vscode.py/QT/Wallpaper And Links/3- FiewWatch.png"))

#     def show2ndphoto(self):
#         self.photo.setPixmap(QtGui.QPixmap("C:/Users/CAVO TECH/Desktop/vscode.py/QT/Wallpaper And Links/wallpaperflare.com_wallpaper"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
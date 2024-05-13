import PyQt6.QtWidgets as qtw
import untitled as unt
from PyQt6 import QtCore, QtGui, QtWidgets


class ahpl (qtw.QMainWindow,unt.Ui_MainWindow):
    def __init__(self):  
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.click.clicked.connect(self.ok)


    def ok (self):
        print(1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 170, 171, 61))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(330, 0, 381, 581))
        self.label_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setMidLineWidth(0)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("../../../Pictures/Saved Pictures/WhatsApp Image 2024-03-03 at 23.56.01_b290bf24.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 361, 581))
        self.label_3.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_3.setMidLineWidth(0)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_3.setPixmap(QtGui.QPixmap("../../../Pictures/Saved Pictures/WhatsApp Image 2024-03-03 at 23.56.51_515de9e7.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label_2.raise_()
    






app = qtw.QApplication([])
win=ahpl()
win.show()
app.exec()
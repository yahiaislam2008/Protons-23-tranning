from PyQt6 import QtGui
import PyQt6.QtWidgets as qtw
import hpdmom as bth
import phmom as ph


class hbthdph (qtw.QMainWindow,ph.Ui_MainWindow):
    def __init__(self):  
        super().__init__()
        self.setupUi(self) 

        self.ph.setShortcut("N")
        self.ph2.setShortcut("B")
        self.ph3.setShortcut("V")
        self.ph4.setShortcut("M")
            
        self.ph5.setShortcut("C")
        self.ph.clicked.connect(self.nextph)
        self.ph2.clicked.connect(self.nextph2)
        self.ph3.clicked.connect(self.nextph3)
        self.ph4.clicked.connect(self.nextph4)
        self.ph5.clicked.connect(self.nextph5)

    def nextph(self):
        print(1)

    def nextph2(self):
        print(2)

    def nextph3(self):
        print(3)

    def nextph4(self):
        print(4)

    def nextph5(self):
        print(5)

class hbthd (qtw.QMainWindow,bth.Ui_m4_lazm_t3rfy):
    def __init__(self):  
        super().__init__()
        self.setupUi(self) 

        self.suprize.clicked.connect(self.openphs)


    def openphs(self):
        global win
        win.close()
        win=hbthdph()
        win.show()
        




app = qtw.QApplication([])
win=hbthd()
win.show()
app.exec()
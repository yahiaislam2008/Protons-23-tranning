import PyQt5.QtWidgets as qtw
import Final as win
# import serial

# ser = serial.Serial("/dev/ttyUSB0",9600)

# us = ser.read()

class final (qtw.QMainWindow, win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.dactance.setText(str(us))
        self.forward.setShortcut("W")
        self.forward.clicked.connect(lambda: self.robo("f"))
        self.lup.setShortcut("I")
        self.lup.clicked.connect(lambda: self.robo("lu"))
        self.ldown.setShortcut("K")
        self.ldown.clicked.connect(lambda: self.robo("ld"))
        self.left.setShortcut("A")
        self.left.clicked.connect(lambda: self.robo("l"))
        self.right.setShortcut("D")
        self.right.clicked.connect(lambda: self.robo("r"))
        self.back.setShortcut("S")
        self.back.clicked.connect(lambda: self.robo("b"))
        self.rup.setShortcut("O")
        self.rup.clicked.connect(lambda: self.robo("ru"))
        self.rdown.setShortcut("L")
        self.rdown.clicked.connect(lambda: self.robo("rd"))
        self.three.setShortcut("3")
        self.three.clicked.connect(lambda: self.robo("3"))
        self.two.setShortcut("2")
        self.two.clicked.connect(lambda: self.robo("2"))
        self.one.setShortcut("1")
        self.one.clicked.connect(lambda: self.robo("1"))

    def robo(self, c):
        print(c)
        return c
        # ser.write(c.encode("ascii")) 
    

app = qtw.QApplication([])
win=final()
win.show()
app.exec()





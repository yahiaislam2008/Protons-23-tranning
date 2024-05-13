import PyQt5.QtWidgets as qtw
import design 

class MainWindow(qtw.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expression = ""
        self.exprion.setText(self.expression)
        self.eqp.setText("")
        self.num1.clicked.connect(lambda: self.addchar("1"))
        self.num2.clicked.connect(lambda: self.addchar("2"))
        self.num3.clicked.connect(lambda: self.addchar("3"))
        self.num4.clicked.connect(lambda: self.addchar("4"))
        self.num5.clicked.connect(lambda: self.addchar("5"))
        self.num6.clicked.connect(lambda: self.addchar("6"))
        self.num7.clicked.connect(lambda: self.addchar("7"))
        self.num8.clicked.connect(lambda: self.addchar("8"))
        self.num9.clicked.connect(lambda: self.addchar("9"))
        self.num0.clicked.connect(lambda: self.addchar("0"))
        self.add.clicked.connect(lambda: self.addchar("+"))
        self.manc.clicked.connect(lambda: self.addchar("-"))
        self.lll.clicked.connect(lambda: self.addchar("/"))
        self.aaa.clicked.connect(lambda: self.addchar("*"))
        self.equel.clicked.connect(self.getresult)
        self.clear.clicked.connect(self.getclear)

    def addchar(self, c):
        self.expression +=c
        self.exprion.setText(self.expression)
    def getresult(self):
        result =str(eval(self.expression))
        self.eqp.setText(result)
    def getclear(self):
        self.expression =""
        self.exprion.setText(self.expression)
        self.eqp.setText("")


app = qtw.QApplication([])
win=MainWindow()
win.show()
app.exec()
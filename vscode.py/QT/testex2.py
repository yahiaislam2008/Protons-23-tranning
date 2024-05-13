from PyQt6 import QtGui
import PyQt6.QtWidgets as qtw
import test2 as t

class fargha (qtw.QMainWindow,t.Ui_MainWindow):
    def __init__(self):  
        super().__init__()
        self.setupUi(self) 

        self.st.clicked.connect(self.stph)
        self.nd.clicked.connect(self.ndph)     
        

    def stph(self):
       print(6)
       self.photo.setPixmap(QtGui.QPixmap("3- FiewWatch.png"))


    def ndph(self):
       print(8)
       self.photo.setPixmap(QtGui.QPixmap("wallpaperflare.com_wallpaper.jpg"))



app = qtw.QApplication([])
f=fargha()
f.show()
app.exec()
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QPushButton
from PyQt5 import uic
import sys



class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("AddItem.ui", self)

        self.show()




app = QApplication(sys.argv)
UIWindows = UI()
app.exec_()




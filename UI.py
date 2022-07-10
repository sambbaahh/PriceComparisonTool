from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QPushButton
from PyQt5 import uic
import sys



class UI(QDialog):

    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("UIcode.py", self)

        self.show()




app = QApplication()
UIWindows = UI()
app.exec_()




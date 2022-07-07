from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5.uic import loadUiType
from os import path
import sys



class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "untitled.ui"))
        self.show()

app = QApplication(sys.argv)
UIWindows = UI()
app.exec_()
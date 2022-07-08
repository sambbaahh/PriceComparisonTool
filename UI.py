from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5 import uic
import sys



class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("Main.ui", self)

        self.show()

app = QApplication(sys.argv)
UIWindows = UI()
app.exec_()
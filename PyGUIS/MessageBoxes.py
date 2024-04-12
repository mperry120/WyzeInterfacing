import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

#           font name, size
font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Message Boxes")

        self.UI()

    def UI(self):
        button = QPushButton("Clicker", self)
        button.setFont(font)
        button.move(10, 10)
        button.clicked.connect(self.messageBox)

        self.show()

    def messageBox(self):
        mBox = QMessageBox()
        mBox.setInformativeText("test")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
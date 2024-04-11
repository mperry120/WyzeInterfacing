import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 450)
        self.setWindowTitle("Window title bar")

        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi Python")
        self.setGeometry(0, 0, 350, 400)
        self.UI()

    def UI(self):
        text1 = QLabel('Hello World', self)
        text2 = QLabel('Goodbye world', self)
        text1.move(10,  10)
        text2.move(10, 30)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
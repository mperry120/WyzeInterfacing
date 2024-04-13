import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        hBox = QHBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")

        hBox.addStretch()

        hBox.addWidget(button1)
        hBox.addWidget(button2)
        hBox.addWidget(button3)


        self.setLayout(hBox)


        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
if __name__ == '__main__':
    main()
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        hbox=QHBoxLayout()
        button1=QPushButton("Button1",self)
        button2=QPushButton("Button2")
        button3=QPushButton("Button3")
        hbox.addStretch()
        hbox.addWidget(button1, alignment=Qt.AlignmentFlag.AlignRight)
        hbox.addWidget(button2, alignment=Qt.AlignmentFlag.AlignCenter)
        hbox.addWidget(button3, alignment=Qt.AlignmentFlag.AlignLeft)
        hbox.addStretch()

        self.setLayout(hbox)
        self.show()


def main():
    App=QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__=='__main__':
    main()
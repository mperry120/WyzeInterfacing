import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi Python")
        self.setGeometry(0, 0, 350, 400)
        self.UI()

    def UI(self):
        self.text = QLabel("Example test", self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)
        self.text.move(160, 50)
        enterButton.move(100, 80)
        exitButton.move(200, 80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)

        self.show()

    def enterFunc(self):
        self.text.setText("Enter pressed")
        self.text.resize(150,20)
    def exitFunc(self):
        self.text.setText("Exit pressed")
        self.text.resize(150,20)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
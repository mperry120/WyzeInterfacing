import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning images")
        self.setGeometry(0, 0, 350, 350)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('Widgets/WyzeLogo.PNG'))
        self.image.setScaledContents(True)
        self.image.setGeometry(10, 10, 200, 200)
        self.image.move(10, 10)
        removeButton = QPushButton("Remove", self)
        removeButton.move(10, 200)
        removeButton.clicked.connect(self.removeImg)
        showButton = QPushButton("Show", self)
        showButton.move(125, 200)
        showButton.clicked.connect(self.showImg)

        self.show()
    
    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
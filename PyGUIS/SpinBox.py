import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

#           font name, size
font = QFont("Times", 20)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Message Boxes")

        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 100)
        self.spinBox.setFont(font)
        
        # self.spinBox.setMinimum(0)
        # self.spinBox.setMaximum(1000)

        self.spinBox.setRange(-10, 200)
        self.spinBox.setPrefix("$")
        self.spinBox.setSuffix("% ")
        self.spinBox.setSingleStep(5)
        self.spinBox.valueChanged.connect(self.getVal)
        button = QPushButton("send it!", self)
        button.move(150, 150)
        button.clicked.connect(self.getVal)



        self.show()
    
    def getVal(self):
        val = self.spinBox.value()
        print(val)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
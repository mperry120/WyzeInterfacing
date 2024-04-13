import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer

#           font name, size
font = QFont("Times", 20)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Timer widgets!")

        self.UI()

    
    def UI(self):
        self.xAxis = QLineEdit(self)
        self.yAxis = QLineEdit(self)
        button = QPushButton("Send It!", self)
        button.move(10, 70)
        button.clicked.connect(self.getVal)
        self.xAxis.move(10, 10)
        self.yAxis.move(10,40)

        self.colorLabel = QLabel(self)
        self.colorLabel.resize(200, 200)
        self.colorLabel.setStyleSheet("background-color:green")
        self.colorLabel.move(150, 150)
        
        btnStart = QPushButton("Start", self)
        btnStop = QPushButton("Stop", self)
        btnStart.move(10, 100)
        btnStop.move(10,130)
        btnStart.clicked.connect(self.strtTimer)
        btnStop.clicked.connect(self.stpTimer)


        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.changeColor)
        self.val = 0

        self.show()
    

    def changeColor(self):
        if self.val == 0:
            self.colorLabel.setStyleSheet("background-color:red")
            self.val = 1
        else:
            self.colorLabel.setStyleSheet("background-color:orange")
            self.val = 0

    def strtTimer(self):
        self.timer.start()

    def stpTimer(self):
        self.timer.stop()

    def getVal(self):
        xVal = self.xAxis.text()
        yVal = self.yAxis.text()
        self.colorLabel.move(int(xVal), int(yVal))

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
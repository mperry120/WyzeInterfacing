import sys
from PyQt6.QtWidgets import *
import func
import os
import datetime

pullDate = '2024-04-01'

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wyze plug power usage")
        self.setGeometry(0, 0, 350, 400)
        self.UI()


    def UI(self):
        self.dateInsert = QLineEdit(self)
        self.dateInsert.setPlaceholderText("YYYY-MM-DD")
        self.dateInsert.move(100, 10)
        button = QPushButton("Submit", self)
        button.move(130, 50)
        button.clicked.connect(self.fetchData)
        self.text = QLabel('', self)
        self.text.move(100,  100)
        self.show()

    def fetchData(self, dateInsert):
        date = self.dateInsert.text()
        WyzeData = func.printDailyString(date)
        self.text.setText(WyzeData)
        self.text.adjustSize()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
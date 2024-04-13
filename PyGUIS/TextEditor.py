import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

#           font name, size
font = QFont("Times", 20)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Text editor")

        self.UI()

    #can it be auto centered? word wrapped? window size adjustable?
    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(120, 150)
        button = QPushButton("Send It!" ,self)
        button.move(220, 350)
        button.clicked.connect(self.getVal)


        self.show()
    
    def getVal(self):
        text = self.editor.toPlainText()
        print(text)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
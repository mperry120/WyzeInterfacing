import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Comboboxes")
        self.setGeometry(100, 100, 350, 350)
        self.UI()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        button = QPushButton("Save", self)
        button.move(150, 130)
        button.clicked.connect(self.getVal)
        self.combo.addItem("Python")
        self.combo.addItems(['1', '2', '3', '4', '5'])
        list1 = ["Batman", "Superman", "Spiderman"]

        for name in list1:
            self.combo.addItem(name)

        for num in range(1, 100):
            self.combo.addItem(str(num))

        self.show()
    
    def getVal(self):
        value = self.combo.currentText()
        print(value, "\n")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
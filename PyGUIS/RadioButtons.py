import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Radio Buttons")

        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(170, 50)
        self.name.setPlaceholderText("Enter your name")
        self.surname = QLineEdit(self)
        self.surname.move(170, 80)
        self.surname.setPlaceholderText("Enter your surname")
        self.male = QRadioButton("Male", self)
        self.male.setChecked(True)
        self.male.move(170, 110)
        self.female = QRadioButton("Female", self)
        self.female.move(240, 110)
        button = QPushButton("Submit", self)
        button.move(170, 140)
        button.clicked.connect(self.getVal)

        self.show()

    def getVal(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print(name, " ", surname, " Male")
        else:
            print(name, " ", surname, " female")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
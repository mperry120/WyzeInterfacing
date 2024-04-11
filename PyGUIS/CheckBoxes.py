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
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter surname")
        self.name.move(105, 50)
        self.surname.move(105, 80)
        self.remember = QCheckBox("Remember me", self)
        self.remember.move(105, 110)
        button = QPushButton("Submit", self)
        button.move(105, 140)
        button.clicked.connect(self.submit)

        self.show()
    

    def submit(self):
        if (self.remember.isChecked()):
            print("Name: " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me = True")
        else:
            print("Name: " + self.name.text() + "\nSurname: " + self.surname.text() + "\nRemember me = False")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
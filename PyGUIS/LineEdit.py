import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learning about line edits.")
        self.setGeometry(0, 0, 350, 400)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText('Please enter your name')
        self.nameTextBox.move(105, 50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText('Please enter your password')
        self.passTextBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.passTextBox.move(105, 80)
        button = QPushButton("Save", self)
        button.move(130, 110)
        button.clicked.connect(self.getValues)
        self.show()
    
    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("Youre name is: " + name + "Your password is: " + password)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
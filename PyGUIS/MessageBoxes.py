import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

#           font name, size
font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Message Boxes")

        self.UI()

    def UI(self):
        button = QPushButton("Clicker", self)
        button.setFont(font)
        button.move(10, 10)
        button.clicked.connect(self.messageBox)

        self.show()

    # #First Workable
    # def messageBox(self):
    #     mBox = QMessageBox(self)
    #     yesButton = mBox.addButton(QMessageBox.StandardButton.Yes)
    #     mBox.exec()
    #     if mBox.clickedButton() == yesButton:
    #         print("TEST")

    #Second Workable
    def messageBox(self):
        mBox = QMessageBox.question(self, 
                                    "Warning", 
                                    "Are you sure you want to exit?", 
                                    buttons=QMessageBox.StandardButton.Yes | 
                                    QMessageBox.StandardButton.Save | 
                                    QMessageBox.StandardButton.Abort | 
                                    QMessageBox.StandardButton.Apply, 
                                    defaultButton= QMessageBox.StandardButton.Abort
                                    )
        if mBox == QMessageBox.StandardButton.Yes:
            print('Clicked Yes')
            extBox = QMessageBox.information(self, "Notice", "Exiting application")
            if extBox == QMessageBox.StandardButton.Ok:
                sys.exit()
            else:
                sys.exit()
        elif mBox == QMessageBox.StandardButton.Save:
            txtBox = QMessageBox.information(self, "Notice", "You clicked Save.. What are you trying to save?")
            print('Clicked Save, but there\'s nothing to save, lol')
        elif mBox == QMessageBox.StandardButton.Abort:
            print('Clicked Abort')
        elif mBox == QMessageBox.StandardButton.Apply:
            txtBox = QMessageBox.information(self, "Notice", "You clicked Apply.. There's nothing to apply...")
            print("Clicked Apply, but there's nothing to apply, lol")
        #bug... doc says it whould return 'escape button' if none of the set standard buttons are clicked but...
        else:
            print('Pressed ESC')        
        
        


        


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
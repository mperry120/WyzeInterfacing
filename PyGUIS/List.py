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
        self.setWindowTitle("List widgets!")

        self.UI()

    
    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100, 50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(100, 80)

        #ADDING NAMES TO LIST
        list = ["Batmatn", "Superman", "Spiderman"]
        self.listWidget.addItems(list)
        self.listWidget.addItem("Thor")

        #ADDING NUMBERS TO LIST
        for num in range(0, 10):
            self.listWidget.addItem(str(num))
        

        btnAdd = QPushButton("Add", self)
        btnAdd.move(360, 80)
        btnAdd.clicked.connect(self.add)
        btnDelete = QPushButton("Delete", self)
        btnDelete.move(360, 110)
        btnDelete.clicked.connect(self.delete)
        btnGet = QPushButton("Get", self)
        btnGet.move(360, 140)
        btnGet.clicked.connect(self.get)
        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.move(360, 170)
        btnDeleteAll.clicked.connect(self.deleteAll)

        self.show()


    def add(self):
        val = self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")

    def delete(self):
        id = self.listWidget.currentRow()
        self.listWidget.takeItem(id)
    
    def get(self):
        val = self.listWidget.currentItem().text()
        print(val)
    
    def deleteAll(self):
        self.listWidget.clear()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()
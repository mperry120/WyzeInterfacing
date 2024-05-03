import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        label.setOpenExternalLinks(True) # This allows opening links in a browser
        label.setTextFormat(Qt.TextFormat.RichText) # Set text format to RichText
        label.setText('<a href="http://www.example.com">Visit Example.com</a>')

        self.setCentralWidget(label)

        self.setWindowTitle("Hyperlink Example")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

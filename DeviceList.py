import os
import sys

import datetime
import time
import calendar
import pprint
import func
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from wyze_sdk.errors import WyzeApiError
from datetime import timedelta


#Set date to pull data from
pullDate = '2024-03-15'


    # email = 'mperry120@gmail.com',
    # password = 'ziJfym-fodsaq-ribwo6',
    # key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    # api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')


try:


    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Horizontal Box Layout")
            self.setGeometry(350,150,400,400)
            self.UI()

        def UI(self):
            mainLayout = QVBoxLayout()
            TopLayout = QVBoxLayout()
            BottomLayout = QVBoxLayout()
            mainLayout.addLayout(TopLayout)
            mainLayout.addLayout(BottomLayout)

            email = QLineEdit()
            email.setPlaceholderText("Email")
            password = QLineEdit()
            password.setPlaceholderText("Password")
            key_id = QLineEdit()
            key_id.setPlaceholderText("Key ID")
            api_key = QLineEdit()
            api_key.setPlaceholderText("API Key")
            button = QPushButton("Enter")
            TopLayout.addStretch()
            TopLayout.addWidget(QLabel("Enter your Wyze credentials:"), alignment=Qt.AlignmentFlag.AlignCenter)

            TopLayout.addWidget(email, alignment=Qt.AlignmentFlag.AlignCenter)
            TopLayout.addWidget(password, alignment=Qt.AlignmentFlag.AlignCenter)
            TopLayout.addWidget(key_id, alignment=Qt.AlignmentFlag.AlignCenter)
            TopLayout.addWidget(api_key, alignment=Qt.AlignmentFlag.AlignCenter)
            TopLayout.addStretch()
            
            hBox = QHBoxLayout()

            BottomLayout.addLayout(hBox)

            hBox.addStretch()
            hBox.addWidget(QCheckBox("Remember Me"))
            hBox.addWidget(button)
            hBox.addStretch()
            
            BottomLayout.addStretch()


            self.setLayout(mainLayout)
            self.show()


    def main():
        App=QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

    if __name__=='__main__':
        main()





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)



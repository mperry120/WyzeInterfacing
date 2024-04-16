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
            self.setWindowTitle("Wyze Data Portal")
            self.setGeometry(350,150,400,400)
            self.setContentsMargins(20,20,20,20)
            self.UI()

        def UI(self):
            mainLayout = QVBoxLayout()
            TopLayout = QVBoxLayout()
            BottomLayout = QVBoxLayout()
            mainLayout.addLayout(TopLayout)
            mainLayout.addLayout(BottomLayout)

            self.email = QLineEdit()
            self.email.setPlaceholderText("Email")
            self.email.setFixedWidth(200)
            self.password = QLineEdit()
            self.password.setPlaceholderText("Password")
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
            self.password.setFixedWidth(200)
            key_id = QLineEdit()
            key_id.setPlaceholderText("Key ID")
            key_id.setFixedWidth(200)
            api_key = QLineEdit()
            api_key.setPlaceholderText("API Key")
            api_key.setFixedWidth(200)
            button = QPushButton("Enter")


            ThBox1 = QHBoxLayout()
            ThBox2 = QHBoxLayout()
            ThBox3 = QHBoxLayout()
            ThBox4 = QHBoxLayout()
            ThBox5 = QHBoxLayout()
            
            ThBox1.addWidget(QLabel("Enter your Wyze credentials:"), alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox2.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox3.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox4.addWidget(key_id, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox5.addWidget(api_key, alignment=Qt.AlignmentFlag.AlignCenter)

            TopLayout.addLayout(ThBox1)
            TopLayout.addLayout(ThBox2)
            TopLayout.addLayout(ThBox3)
            TopLayout.addLayout(ThBox4)
            TopLayout.addLayout(ThBox5)
            TopLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)            

            hBox = QHBoxLayout()
            BottomLayout.addLayout(hBox)

            self.rememberMe = QCheckBox("Remember Me")
            hBox.addWidget(self.rememberMe, alignment=Qt.AlignmentFlag.AlignRight)
            hBox.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
            BottomLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

            button.clicked.connect(self.pressEnter)




            f = open("SaveData.txt")
            if f.read() != "":
                content = f.readlines()
                self.email.setText(content[0])
                self.password.setText(content[1])
                print(content)
                f.close()
            else:
                f.close()





            # f = open("SaveData.txt", "r")
            # self.email.setText(f.read())
            # f.close()
            


            self.setLayout(mainLayout)
            self.show()

        def pressEnter(self):
            if self.rememberMe.isChecked():
                f = open("SaveData.txt", "w")
                f.write(self.email.text(), "\n")
                f.write(self.password.text(), "\n")
                f.close()
            else:
                f = open("SaveData.txt", "w")
                f.write("")
                f.close()
            

#I what the remember me checkbox to stay checked if the user has checked it before




            # password = password.text()
            # key_id = key_id.text()
            # api_key = api_key.text()
            # rememberMe = rememberMe.isChecked()
            print(self.email.text())
            # SaveData.saveData(email, password, key_id, api_key, rememberMe)
            # self.close()

    def main():
        App=QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

    if __name__=='__main__':
        main()





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)



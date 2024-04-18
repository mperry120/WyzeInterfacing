import os
import sys
import datetime
import time
import calendar
import pprint
import func
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from wyze_sdk.errors import WyzeApiError
from datetime import timedelta


#Set date to pull data from
pullDate = '2024-03-15'


    # email = 'mperry120@gmail.com',
    # password = 'ziJfym-fodsaq-ribwo6',
    # key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    # api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')

font = QFont("Times", 10)


try:


    class usageWindow(QWidget):
        def __init__(self, mac):
            super().__init__()
            func.setPlugData(mac)
            self.setWindowTitle("Wyze Data Portal - Power Usage")
            self.setGeometry(350,150,600,400)
            self.setContentsMargins(20,20,20,20)
            
            mainLayout = QVBoxLayout()
            usageText = QTextEdit(self)
            usageText.setReadOnly(True)
            usageText.setFont(font)
            usageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
            usageText.setText(func.printDaily(pullDate))
            mainLayout.addWidget(usageText)
            

            self.setLayout(mainLayout)

            

    class newWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Wyze Data Portal - Device List")
            self.setGeometry(350,150,600,400)
            self.setContentsMargins(20,20,20,20)
            mainLayout = QHBoxLayout()
            leftLayout = QVBoxLayout()
            leftLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            rightLayout = QVBoxLayout()
            deviceListTitle = QLabel("Device List")
            deviceListTitle.setFont(font)
            leftLayout.addWidget(deviceListTitle)
            deviceListTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.deviceList = QTextEdit(self)
            self.deviceList.setFixedWidth(200)
            self.deviceList.setReadOnly(True)
            self.deviceList.setFont(font)
            self.deviceList.setText("Device List")
            leftLayout.addWidget(self.deviceList)
            self.deviceList.setText(func.getDeviceList())

            daily = QRadioButton("Daily")
            weekly = QRadioButton("Weekly")
            monthly = QRadioButton("Monthly")
            rightLayout.addWidget(daily)
            rightLayout.addWidget(weekly)
            rightLayout.addWidget(monthly)

            
            self.errorLabel = QLabel("")
            self.errorLabel.setFont(font)
            self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            rightLayout.addWidget(self.errorLabel)
            self.macAddress = QLineEdit(self)
            self.macAddress.setPlaceholderText("Mac Address")

            

            enterButton = QPushButton("Enter")
            enterButton.setFont(font)

            rightLayout.addWidget(self.macAddress)
            rightLayout.addWidget(enterButton)
            enterButton.clicked.connect(self.getUsageData)

            mainLayout.addLayout(leftLayout)
            mainLayout.addLayout(rightLayout)
            rightLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            self.setLayout(mainLayout)
        
        def getUsageData(self):
            if self.macAddress.text() != "":
                self.usageWindow = usageWindow(self.macAddress.text())
                self.usageWindow.show()
            else:
                self.errorLabel.setText("Please enter a Mac Address")
            # self.usageWindow = usageWindow()
            # self.usageWindow.show()
            # self.window().close()

    class Window(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Wyze Data Portal")
            self.setGeometry(350,150,400,400)
            self.setContentsMargins(20,20,20,20)
            self.UI()


        def UI(self):
            self.mainLayout = QVBoxLayout()
            TopLayout = QVBoxLayout()
            BottomLayout = QVBoxLayout()
            self.mainLayout.addLayout(TopLayout)
            self.mainLayout.addLayout(BottomLayout)

            self.email = QLineEdit()
            self.email.setPlaceholderText("Email")
            self.email.setFixedWidth(200)
            self.password = QLineEdit()
            self.password.setPlaceholderText("Password")
            self.password.setEchoMode(QLineEdit.EchoMode.Password)
            self.password.setFixedWidth(200)
            self.key_id = QLineEdit()
            self.key_id.setPlaceholderText("Key ID")
            self.key_id.setFixedWidth(200)
            self.api_key = QLineEdit()
            self.api_key.setPlaceholderText("API Key")
            self.api_key.setFixedWidth(200)
            button = QPushButton("Enter")


            ThBox1 = QHBoxLayout()
            ThBox2 = QHBoxLayout()
            ThBox3 = QHBoxLayout()
            ThBox4 = QHBoxLayout()
            ThBox5 = QHBoxLayout()
            
            ThBox1.addWidget(QLabel("Enter your Wyze credentials:"), alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox2.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox3.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox4.addWidget(self.key_id, alignment=Qt.AlignmentFlag.AlignCenter)
            ThBox5.addWidget(self.api_key, alignment=Qt.AlignmentFlag.AlignCenter)

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


            self.rememberMe.setChecked(func.get_rememberMe('SaveData.txt'))


            self.email.setText(func.get_email('SaveData.txt'))
            self.password.setText(func.get_password('SaveData.txt'))
            self.key_id.setText(func.get_key_id('SaveData.txt'))
            self.api_key.setText(func.get_api_key('SaveData.txt'))


            self.setLayout(self.mainLayout)
            self.show()

        def pressEnter(self):
            if self.rememberMe.isChecked():
                f = open("SaveData.txt", "w")
                lineToWrite = "email: " + self.email.text() + "\n"
                f.write(lineToWrite)
                lineToWrite = "password: " + self.password.text() + "\n"
                f.write(lineToWrite)
                lineToWrite = "key_id: " + self.key_id.text() + "\n"
                f.write(lineToWrite)
                lineToWrite = "api_key: " + self.api_key.text() + "\n"
                f.write(lineToWrite)
                lineToWrite = "rememberMe: true\n"
                f.write(lineToWrite)
                f.close()
            else:
                f = open("SaveData.txt", "w")
                f.write("")
                f.close()
            self.deviceListWindow = newWindow()
            self.deviceListWindow.show()
            #Seems to work, but I'm not sure if it's the best way to do it
            self.window().close()
            
        


    def main():
        App=QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

    if __name__=='__main__':
        main()





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)



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
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


#Set date to pull data from
pullDate = '2024-04-20'


    # email = 'mperry120@gmail.com',
    # password = 'ziJfym-fodsaq-ribwo6',
    # key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    # api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')

font = QFont("Times", 10)


try:


    #ADD FUNCTIONALITY FOR MULTIPLE GRAPH/READOUT WINDOWS
    #ADD FUNCTIONALITY FOR DAILY/WEEKLY/MONTHLY DATA
    #REFACTOR DEVICE DATA LIST PAGE FOR BETTER CLARITY ON WHICH DEVICES CAN PROVIDE ENERGY USAGE DATA
    #ADD FUNCTIONALITY FOR SELECTABLE START DATE FOR DATA PULL... THINK ABOUT WHETHER OR NOT TO ALLOW FOR END DATE
    class usageWindow(QWidget):
        def __init__(self, mac):
            super().__init__()

            func.setPlugData(mac)
            
            self.setWindowTitle("Wyze Data Portal - Power Usage")
            self.setGeometry(350, 150, 600, 400)
            self.setContentsMargins(20, 20, 20, 20)


            dataDict = func.getDaily(pullDate)
            dataString = func.dictString(dataDict)

            x, y1 = func.dictList(dataDict)

            # Convert datetime.date objects to floating point numbers
            x_timestamp = [datetime.datetime.fromordinal(date.toordinal()).timestamp() for date in x]


            mainLayout = QVBoxLayout()
            self.tabs = QTabWidget()
            self.tab1 = QWidget()
            self.tab2 = QWidget()
            self.tabs.addTab(self.tab1, "ReadOut")
            self.tabs.addTab(self.tab2, "Graph")

            usageText = QTextEdit(self)
            usageText.setReadOnly(True)
            usageText.setFont(font)
            usageText.setAlignment(Qt.AlignmentFlag.AlignCenter)

            usageText.setText(dataString)

            readOutLayout = QVBoxLayout()
            readOutLayout.addWidget(usageText)
            self.tab1.setLayout(readOutLayout)

            xTest = [1.1, 2.9, 3.1, 4.6, 5.2, 6.1, 7.4, 8.6, 9.4, 10.8]
            yTest = [5.4, 5.3, 7.4, 10.1, 3.0, 8.8, 9.4, 1.2, 6.7, 2.1]
            print(xTest, '\n', yTest, '\n', x_timestamp, '\n', y1)
            xTest2 = []
            for i in x_timestamp:
                xTest2.append(i/1000)
            print(xTest2)

            graph = pg.PlotWidget()
            graph.showGrid(x=True, y=True)
            gphTitle = 'Power Usage'
            graph.setLabel('bottom', (pullDate + ' - present'))
            graph.setLabel('left', 'Power Usage (KWh)')

            # # Plotting the data
            # plot = graph.plot(x_timestamp, y1, pen='g', name=gphTitle)

            # Set x-axis ticks and labels to display dates
            date_strings = [date.strftime('%m-%d') for date in x]
            ticks = [(x_timestamp[i], date_strings[i]) for i in range(len(x))]

            

            # Set max number of ticks to display
            max_ticks = 10
            if len(ticks) > max_ticks:
                # If there are too many ticks, hide the tick text
                for i, tick in enumerate(ticks):
                    if i % 2 == 0:
                        ticks[i] = (tick[0], '')
                # graph.getAxis('bottom').setStyle(showValues=False)

            graph.getAxis('bottom').setTicks([ticks])

            axis = pg.DateAxisItem()
            graph.setAxisItems({'bottom': axis})

            barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=50000, brush='c')
            graph.addItem(barGraph)


            graphLayout = QVBoxLayout()
            graphLayout.addWidget(graph)
            self.tab2.setLayout(graphLayout)

            mainLayout.addWidget(self.tabs)
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



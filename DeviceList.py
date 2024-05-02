import os
import sys
import datetime
import func
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from wyze_sdk.errors import WyzeApiError
from datetime import timedelta
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDateEdit



#Set date to pull data from
pullDate = '2024-04-01'


    # email = 'mperry120@gmail.com',
    # password = 'ziJfym-fodsaq-ribwo6',
    # key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    # api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')

font = QFont("Courier", 10)
errorFont = QFont("Times", 12, QFont.Weight.Bold)

try:







    #ADD FUNCTIONALITY FOR SELECTABLE END DATE FOR DATA PULL.
        #DONE, HOWEVER THE WEEKLY READOUT IS QUIRKY..
            #Wasn't done. Was full of bugs. But now it'd really done.. Maybe.. the funk do I know?


    #ADD (OPTIONAL?) FUNCTIONALITY OF PEAK HOURS/OFF PEAK HOURS SUMS. this one next.

    #ADD A GRAPHIC OR LOGO.
    #ADD A LINK TO THE WYZE API KEY PAGE.
    #ADD FUNCTIONALITY TO CREDENTIALS ENTRY & REMEMBER TO HANDLE EXCEPTIONS.
    class usageWindow(QWidget):
        def __init__(self, mac, xCoord, yCoord):
            super().__init__()

            typeCheck = func.setPlugData(mac)
            if typeCheck == None:
                self.setWindowTitle("Whoopsie")
                #self.setGeometry(350, 150, 225, 100)
                self.setGeometry(xCoord + 200, yCoord + 100, 225, 100)
                self.setContentsMargins(20, 20, 20, 20)
                mainLayout = QVBoxLayout()
                errorMessage = QLabel("Device not found")
                errorMessage.setStyleSheet("color: red")
                errorMessage.setFont(errorFont)
                errorMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainLayout.addWidget(errorMessage)
                self.setLayout(mainLayout)
                self.show()

            
            else:
                self.setWindowTitle("Wyze Data Portal - Power Usage")
                self.setGeometry(xCoord + 220, yCoord + 30, 600, 400)
                self.setContentsMargins(20, 20, 20, 20)


                mainLayout = QVBoxLayout()
                self.tabs = QTabWidget()
                self.tabs.setTabsClosable(True)
                self.tabs.tabCloseRequested.connect(self.removeTab)
                self.tab1 = QWidget()
                # self.tab2 = QWidget()
                # self.tab3 = QWidget()
                self.tabs.addTab(self.tab1, "Settings")
                # self.tabs.addTab(self.tab2, "ReadOut")
                # self.tabs.addTab(self.tab3, "Graph")



                #Settings Tab
                settingsLayout = QHBoxLayout()
                leftLayout = QVBoxLayout()
                centerLayout = QVBoxLayout()
                rightLayout = QVBoxLayout()
                settingsLayout.addLayout(leftLayout)
                settingsLayout.addLayout(centerLayout)
                settingsLayout.addLayout(rightLayout)
                leftLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                rightLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)


                #Center Layout
                #Layout structure:
                #Main Vertical Layout in center
                centerVLayout = QVBoxLayout()

                #3 Horizontal Layouts within the main vertical layout
                centerVHLayout1 = QHBoxLayout()
                centerVHLayout2 = QHBoxLayout()
                centerVHLayout3 = QHBoxLayout()

                #one more vertical Layout within centerVHLayout2 that contains the radio buttons
                centerVvLayout1 = QVBoxLayout()

                #Make it so
                centerVHLayout2.addLayout(centerVvLayout1)
                centerVHLayout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                centerVLayout.addLayout(centerVHLayout1)
                centerVLayout.addLayout(centerVHLayout2)
                centerVLayout.addLayout(centerVHLayout3)
                centerLayout.addLayout(centerVLayout)

                instructions = QLabel("Select dates for the data pull\nand choose the data format")
                instructions.setFont(font)
                centerVHLayout1.addWidget(instructions)
                centerVHLayout1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tab1.setLayout(settingsLayout)

                #Create radio buttons for daily, weekly, and monthly data
                self.hourlyButton = QRadioButton("Hourly Data")
                self.hourlyButton.setFont(font)
                self.dailyButton = QRadioButton("Daily Data")
                self.dailyButton.setFont(font)
                self.weeklyButton = QRadioButton("Weekly Data")
                self.weeklyButton.setFont(font)
                self.monthlyButton = QRadioButton("Monthly Data")
                self.monthlyButton.setFont(font)

                #Create a button group for the radio buttons
                #Why do I want a button group?
                #I want a button group so that only one radio button can be selected at a time... lol AI
                buttonGroup = QButtonGroup()
                buttonGroup.addButton(self.hourlyButton)
                buttonGroup.addButton(self.dailyButton)
                buttonGroup.addButton(self.weeklyButton)
                buttonGroup.addButton(self.monthlyButton)

                #Add buttons to the layout
                centerVvLayout1.addWidget(self.hourlyButton)
                centerVvLayout1.addWidget(self.dailyButton)
                centerVvLayout1.addWidget(self.weeklyButton)
                centerVvLayout1.addWidget(self.monthlyButton)



                #Create Enter button and align to the center of the tab
                enterButton1 = QPushButton("Enter")
                enterButton1.setFont(font)
                centerVHLayout3.addWidget(enterButton1)
                centerVHLayout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                enterButton1.setMaximumWidth(100)

                #PHASE OUT
                #enterButton.clicked.connect(self.testFunc)
                #PHASE OUT



                #Left Layout
                startDateLabel = QLabel("Start Date")
                startDateLabel.setFont(font)
                leftLayout.addWidget(startDateLabel)

                self.startDate = QDateEdit(self)
                self.startDate.setCalendarPopup(True)
                self.startDate.setDisplayFormat('MM-dd-yyyy')
                self.startDate.setDate(QDate.currentDate().addDays(-7))
                self.startDate.setFixedWidth(200)
                self.startDate.setMaximumDate(QDate.currentDate())
                leftLayout.addWidget(self.startDate)

                #Right Layout
                startDateLabel = QLabel("End Date")
                startDateLabel.setFont(font)
                rightLayout.addWidget(startDateLabel)

                self.endDate = QDateEdit(self)
                self.endDate.setCalendarPopup(True)
                self.endDate.setDisplayFormat('MM-dd-yyyy')
                self.endDate.setDate(QDate.currentDate())
                self.endDate.setFixedWidth(200)
                self.endDate.setMaximumDate(QDate.currentDate())
                rightLayout.addWidget(self.endDate)



                # Enter button clicked
                enterButton1.clicked.connect(self.checkDates)


                mainLayout.addWidget(self.tabs)
                self.setLayout(mainLayout)

            self.close()

        def checkDates(self):
            # Make sure the Start date is befor the End date
            # Convert Datetime.date objs into timestamps
            sDate = self.startDate.date()
            eDate = self.endDate.date()
            datetimeObj = datetime.datetime(sDate.year(), sDate.month(), sDate.day())
            datetimeObj2 = datetime.datetime(eDate.year(), eDate.month(), eDate.day())
            sTimeStamp = datetimeObj.timestamp()
            eTimeStamp = datetimeObj2.timestamp()
            if sTimeStamp > eTimeStamp:
                errorBox = QMessageBox()
                errorBox.setText("Start date cannot be after the End date")
                errorBox.exec()
            else:
                self.createTabs(self.startDate.date().toString('yyyy-MM-dd'), self.endDate.date().toString('yyyy-MM-dd'))


        def test(self):
            print("test... please work...")

        def createTabs(self, startDate, endDate):
            # try:
            format = None
            if self.hourlyButton.isChecked():
                dataDict = func.getHourly(startDate, endDate)
                dataString = func.dictStringHourly(dataDict)
                format = "Hourly"
            elif self.dailyButton.isChecked():
                dataDict = func.getDaily(startDate, endDate)
                dataString = func.dictString(dataDict)
                format = "Daily"
            elif self.weeklyButton.isChecked():
                dataDict = func.getWeekly(startDate, endDate)
                dataString = func.dictStringWeekly(dataDict)
                format = "Weekly"
            elif self.monthlyButton.isChecked():
                dataDict = func.getMonthly(startDate, endDate)
                dataString = func.dictStringMonthly(dataDict)
                format = "Monthly"


            # Create readout tab
            self.tab1 = QWidget()
            self.tabs.addTab(self.tab1, format + " Readout")
            usageText = QTextEdit(self)
            usageText.setReadOnly(True)
            usageText.setFont(font)
            usageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
            usageText.setText(dataString)

            readOutLayout = QVBoxLayout()
            readOutLayout.addWidget(usageText)
            self.tab1.setLayout(readOutLayout)

            # Create graph tab
            
            if self.hourlyButton.isChecked():
                self.tab2 = QWidget()
                self.tabs.addTab(self.tab2, format + " Graph")

                x, y1, = func.dictList(dataDict)

                # Convert datetime.datetime objs to timestamps
                x_timestamp = [dateHour.timestamp() for dateHour in x]
                
                # Create plot & set atributes
                graph = pg.PlotWidget()
                graph.showGrid(x=True, y=True)
                graph.setLabel('bottom', (startDate + endDate))
                graph.setLabel('left', 'Power Usage (KWh)')

                # Create dropdown menu to selelct the max Y value for the graph
                maxYselector = QComboBox()
                maxYselector.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '1', '2', '3', '4', '5'])

                # Get max value for Y axis
                maxVal = 0
                for val in dataDict.values():
                    if val / 1000 > maxVal:
                        maxVal = val / 1000
                
                # Create an auto-resize button for Y-axis
                autoResizeButton = QPushButton('Auto \nResize')
                autoResizeButton.setFont(font)
                autoResizeButton.clicked.connect(lambda: graph.setYRange(0, maxVal))

                # Set parameters for graph X-axis
                axis = pg.DateAxisItem()
                graph.setAxisItems({'bottom': axis})
                barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=850, brush='c')
                graph.addItem(barGraph)

                maxYselector.currentIndexChanged.connect(lambda: graph.setYRange(0, float(maxYselector.currentText())))


                # Assign layouts
                mainGraphLayout = QHBoxLayout()
                graphLayout = QVBoxLayout()
                setterLayout = QVBoxLayout()
                graphLayout.addWidget(graph)
                setterLayout.addWidget(autoResizeButton)
                setterLayout.addWidget(maxYselector)
                setterLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainGraphLayout.addLayout(graphLayout)
                mainGraphLayout.addLayout(setterLayout)
                self.tab2.setLayout(mainGraphLayout)

            elif self.dailyButton.isChecked():

                self.tab2 = QWidget()
                self.tabs.addTab(self.tab2, format + " Graph")

                x, y1 = func.dictList(dataDict)

                # Convert datetime.date objects to floating point numbers
                #GET RID OF THE FROMORDINAL() BULLSHIT
                x_timestamp = [datetime.datetime.fromordinal(date.toordinal()).timestamp() for date in x]

                graph = pg.PlotWidget()
                graph.showGrid(x=True, y=True)
                graph.setLabel('bottom', (pullDate + ' - present'))
                graph.setLabel('left', 'Power Usage (KWh)')

                # Create dropdown menu to selelct the max Y value for the graph
                maxYselector = QComboBox()
                maxYselector.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '1', '2', '3', '4', '5'])

                # Get max value for Y axis
                maxVal = 0
                for val in dataDict.values():
                    if val / 1000 > maxVal:
                        maxVal = val / 1000

                # Create an auto-resize button for Y-axis
                autoResizeButton = QPushButton('Auto \nResize')
                autoResizeButton.setFont(font)
                autoResizeButton.clicked.connect(lambda: graph.setYRange(0, maxVal))

                # Set parameters for graph x-axis
                axis = pg.DateAxisItem()
                graph.setAxisItems({'bottom': axis})
                barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=15000, brush='c')
                graph.addItem(barGraph)

                maxYselector.currentIndexChanged.connect(lambda: graph.setYRange(0, float(maxYselector.currentText())))


                # Assign layouts
                mainGraphLayout = QHBoxLayout()
                graphLayout = QVBoxLayout()
                setterLayout = QVBoxLayout()
                graphLayout.addWidget(graph)
                setterLayout.addWidget(autoResizeButton)
                setterLayout.addWidget(maxYselector)
                setterLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainGraphLayout.addLayout(graphLayout)
                mainGraphLayout.addLayout(setterLayout)
                self.tab2.setLayout(mainGraphLayout)

            elif self.weeklyButton.isChecked():
                self.tab2 = QWidget()
                self.tabs.addTab(self.tab2, format + " Graph")

                xTuple, ytemp = func.dictList(dataDict)
                y1 = [val / 1000 for val in ytemp]


                x = [datetime.datetime.strptime(f'{year}-{week}-4', '%Y-%W-%w').date() for year, week in xTuple]


                # Convert datetime.date objects to floating point numbers
                x_timestamp = [datetime.datetime.fromordinal(date.toordinal()).timestamp() for date in x]

                graph = pg.PlotWidget()
                graph.showGrid(x=True, y=True)
                graph.setLabel('bottom', (pullDate + ' - present'))
                graph.setLabel('left', 'Power Usage (KWh)')

                # Create dropdown menu to selelct the max Y value for the graph
                maxYselector = QComboBox()
                maxYselector.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '1', '2', '3', '4', '5'])

                # Get max value for Y axis
                maxVal = 0
                for val in dataDict.values():
                    if val / 1000 > maxVal:
                        maxVal = val / 1000

                # Create an auto-resize button for Y-axis
                autoResizeButton = QPushButton('Auto \nResize')
                autoResizeButton.setFont(font)
                autoResizeButton.clicked.connect(lambda: graph.setYRange(0, maxVal))

                # Set parameters for graph x-axis
                axis = pg.DateAxisItem()
                graph.setAxisItems({'bottom': axis})
                barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=525000, brush='c')
                graph.addItem(barGraph)

                maxYselector.currentIndexChanged.connect(lambda: graph.setYRange(0, float(maxYselector.currentText())))


                # Assign layouts
                mainGraphLayout = QHBoxLayout()
                graphLayout = QVBoxLayout()
                setterLayout = QVBoxLayout()
                graphLayout.addWidget(graph)
                setterLayout.addWidget(autoResizeButton)
                setterLayout.addWidget(maxYselector)
                setterLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainGraphLayout.addLayout(graphLayout)
                mainGraphLayout.addLayout(setterLayout)
                self.tab2.setLayout(mainGraphLayout)

            elif self.monthlyButton.isChecked():
                self.tab2 = QWidget()
                self.tabs.addTab(self.tab2, format + " Graph")

                x, y1 = func.dictList(dataDict)





                # Convert datetime.date objects to floating point numbers
                #GET RID OF THE FROMORDINAL() BULLSHIT
                x_timestamp = [datetime.datetime.fromordinal(date.toordinal()).timestamp() for date in x]

                graph = pg.PlotWidget()
                graph.showGrid(x=True, y=True)
                graph.setLabel('bottom', (pullDate + ' - present'))
                graph.setLabel('left', 'Power Usage (KWh)')

                # Create dropdown menu to selelct the max Y value for the graph
                maxYselector = QComboBox()
                maxYselector.addItems(['0.1', '0.2', '0.3', '0.4', '0.5', '1', '2', '3', '4', '5'])

                # Get max value for Y axis
                maxVal = 0
                for val in dataDict.values():
                    if val / 1000 > maxVal:
                        maxVal = val / 1000

                # Create an auto-resize button for Y-axis
                autoResizeButton = QPushButton('Auto \nResize')
                autoResizeButton.setFont(font)
                autoResizeButton.clicked.connect(lambda: graph.setYRange(0, maxVal))

                # Set parameters for graph x-axis
                axis = pg.DateAxisItem()
                graph.setAxisItems({'bottom': axis})
                barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=150000, brush='c')
                graph.addItem(barGraph)

                maxYselector.currentIndexChanged.connect(lambda: graph.setYRange(0, float(maxYselector.currentText())))


                # Assign layouts
                mainGraphLayout = QHBoxLayout()
                graphLayout = QVBoxLayout()
                setterLayout = QVBoxLayout()
                graphLayout.addWidget(graph)
                setterLayout.addWidget(autoResizeButton)
                setterLayout.addWidget(maxYselector)
                setterLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainGraphLayout.addLayout(graphLayout)
                mainGraphLayout.addLayout(setterLayout)
                self.tab2.setLayout(mainGraphLayout)


            # except Exception as e:
            #     s = str(e)
            #     excType, excObj, excTb = sys.exc_info()
            #     fname = os.path.split(excTb.tb_frame.f_code.co_filename)[1]
            #     # Create errorer message window
            #     errorBox = QMessageBox()
            #     if s == "list index out of range":
            #         errorBox.setText(s + "\nDue to the goofy way in which Wyze groups their data,\nsame day start and end dates my return unexpected results\nor in this case, an error. Please try again with different dates.")
            #         errorBox.exec()
            #     else:
            #         errorBox.setText(s + "\n" + str(excType) + "\n" + fname + "\n" + str(excTb.tb_lineno))
            #         errorBox.exec()
            #     print(sys.exc_info())
                



                # self.errorLabel = QLabel(Exception.args[0])
                # print(Exception.args[0])
                # self.errorLabel.setFont(errorFont)
                # self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                # self.tab1.layout().addWidget(self.errorLabel)

            def testFunc(self):
                # ARGUMENTS NEEDED: (PULL STARTDATE, PULL ENDDATE, (DATA FORMATED DAILY, WEEKLY, OR MONTHLY))
                # Collate hourly data
                dataDict = func.getHourly(pullDate)
                dataString = func.dictStringHourly(dataDict)

                # Create hourly readout tab
                self.tab4 = QWidget()
                self.tabs.addTab(self.tab4, "Hourly Printout")
                usageText = QTextEdit(self)
                usageText.setReadOnly(True)
                usageText.setFont(font)
                usageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
                usageText.setText(dataString)

                readOutLayout = QVBoxLayout()
                readOutLayout.addWidget(usageText)
                self.tab4.setLayout(readOutLayout)

                # Create hourly graph tab
                self.tab5 = QWidget()
                self.tabs.addTab(self.tab5, "Hourly Graph")

                x, y1 = func.dictList(dataDict)

                # Convert datetime.datetime objects to timestamps
                x_timestamp = [dateHour.timestamp() for dateHour in x]

                graph = pg.PlotWidget()
                graph.showGrid(x=True, y=True)
                graph.setLabel('bottom', (pullDate + ' - present'))
                graph.setLabel('left', 'Power Usage (KWh)')

                # Create a dropdown menu to select the max Y value for the graph
                maxYselector = QComboBox()
                maxYselector.addItems(['0.5', '1', '2', '3', '4', '5'])

                # Get the max value for the Y axis
                maxVal = 0
                for val in dataDict.values():
                    if val / 1000 > maxVal:
                        maxVal = val / 1000
                print(maxVal)

                # Create an auto-resize button for y-axis
                autoResizeButton = QPushButton("Resize")
                autoResizeButton.setFont(font)
                autoResizeButton.clicked.connect(lambda: graph.setYRange(0, maxVal))

                # Set parameters for graph x-axis
                axis = pg.DateAxisItem()
                graph.setAxisItems({'bottom': axis})
                barGraph = pg.BarGraphItem(x=x_timestamp, height=y1, width=850, brush='c')
                graph.addItem(barGraph)

                maxYselector.currentIndexChanged.connect(lambda: graph.setYRange(0, float(maxYselector.currentText())))

                


                mainGraphLayout = QHBoxLayout()
                graphLayout = QVBoxLayout()
                setterLayout = QVBoxLayout()
                graphLayout.addWidget(graph)
                setterLayout.addWidget(autoResizeButton)
                setterLayout.addWidget(maxYselector)
                setterLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                mainGraphLayout.addLayout(graphLayout)
                mainGraphLayout.addLayout(setterLayout)
                self.tab5.setLayout(mainGraphLayout)

        def removeTab(self, index):
            self.tabs.removeTab(index)


    class deviceListWindow(QWidget):
        def __init__(self, xCoord, yCoord):
            super().__init__()
            self.setWindowTitle("Wyze Data Portal - Device List")
            self.setGeometry(xCoord - 90, yCoord - 10, 600, 400)
            self.setContentsMargins(20, 20, 20, 20)
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

            self.infoLabel = QLabel("Currently, the only devices\nsupported are the Outdoor Plugs\nModel: WLPP0")
            self.infoLabel.setFont(font)
            self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            rightLayout.addWidget(self.infoLabel)
            
            self.errorLabel = QLabel("")
            self.errorLabel.setFont(font)
            self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            rightLayout.addWidget(self.errorLabel)
            self.macAddress = QLineEdit(self)
            self.macAddress.setPlaceholderText("Mac Address")
            if func.is_remembered("SaveData.txt"):
                self.macAddress.setText(func.get_last_mac("SaveData.txt"))
            

            

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
            #append lineToWrite to SaveData.txt
            if func.is_remembered("SaveData.txt"):
                func.replaceLine("SaveData.txt", "last_mac:", self.macAddress.text())

            if self.macAddress.text() != "":

                xCoord = self.geometry().getCoords()[0]
                yCoord = self.geometry().getCoords()[1]
                self.usageWindow = usageWindow(self.macAddress.text(), xCoord, yCoord)
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
                if func.is_remembered("SaveData.txt"):
                    func.replaceLine("SaveData.txt", "email:", self.email.text())
                    func.replaceLine("SaveData.txt", "password:", self.password.text())
                    func.replaceLine("SaveData.txt", "key_id:", self.key_id.text())
                    func.replaceLine("SaveData.txt", "api_key:", self.api_key.text())
                    func.replaceLine("SaveData.txt", "rememberMe:", "true")
                else:
                    f = open("SaveData.txt", "w")
                    f.write("email: " + self.email.text() + "\n")
                    f.write("password: " + self.password.text() + "\n")
                    f.write("key_id: " + self.key_id.text() + "\n")
                    f.write("api_key: " + self.api_key.text() + "\n")
                    f.write("rememberMe: true")
                    f.close()
            else:
                f = open("SaveData.txt", "w")
                f.write("")
                f.close()
            xCoord = self.geometry().getCoords()[0]
            yCoord = self.geometry().getCoords()[1]
            self.deviceListWindow = deviceListWindow(xCoord, yCoord)
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



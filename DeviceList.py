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
import requests.exceptions
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QIcon



#Set date to pull data from
pullDate = '2024-04-01'

font = QFont("Courier", 10)
errorFont = QFont("Times", 12, QFont.Weight.Bold)

try:

    class usageWindow(QWidget):
        def __init__(self, mac, xCoord, yCoord):
            super().__init__()

            typeCheck = func.setPlugData(mac)
            if typeCheck == None:
                self.setWindowTitle("Whoopsie")
                #self.setGeometry(350, 150, 225, 100)
                self.setGeometry(xCoord + 200, yCoord + 100, 225, 100)
                self.setContentsMargins(20, 20, 20, 20)
                self.setWindowIcon(QIcon('Widgets/WyzeLogo.PNG'))

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
                self.setWindowIcon(QIcon('Widgets/WyzeLogo.PNG'))

                mainLayout = QVBoxLayout()
                self.tabs = QTabWidget()
                self.tabs.setTabsClosable(True)
                self.tabs.tabCloseRequested.connect(self.removeTab)
                self.tab1 = QWidget()
                self.tabs.addTab(self.tab1, "Settings")

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

                instructions = QLabel("Select dates and\n choose format")
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
                self.dailyButton.setChecked(True)

                #Add buttons to the layout
                centerVvLayout1.addWidget(self.hourlyButton)
                centerVvLayout1.addWidget(self.dailyButton)
                centerVvLayout1.addWidget(self.weeklyButton)
                centerVvLayout1.addWidget(self.monthlyButton)

                #Create Start/End date labels and date selectors
                self.peakHourStart = QComboBox()
                self.peakHourStop = QComboBox()
                for i in range(0, 24):
                    self.peakHourStart.addItem(str(i))
                    self.peakHourStop.addItem(str(i))
                centerVvLayout1.addWidget(self.peakHourStart)
                centerVvLayout1.addWidget(self.peakHourStop)
                self.peakHourStart.setCurrentIndex(16)
                self.peakHourStop.setCurrentIndex(21)
                peakStartHBox = QHBoxLayout()
                peakStopHBox = QHBoxLayout()
                peakHoursLabelHbox = QHBoxLayout()
                peakHoursLabel = QLabel("Peak Hours")
                peakHoursLabel.setFont(font)
                peakHoursLabelHbox.addWidget(peakHoursLabel)
                peakStartHBox.addWidget(QLabel("Start"))
                peakStartHBox.addWidget(self.peakHourStart)
                peakStopHBox.addWidget(QLabel("End"))
                peakStopHBox.addWidget(self.peakHourStop)
                peakHoursLabelHbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
                centerVvLayout1.addSpacing(20)
                centerVvLayout1.addLayout(peakHoursLabelHbox)
                centerVvLayout1.addLayout(peakStartHBox)
                centerVvLayout1.addLayout(peakStopHBox)

                #Create Enter button and align to the center of the tab
                enterButton1 = QPushButton("Enter")
                enterButton1.setFont(font)
                centerVHLayout3.addWidget(enterButton1)
                centerVHLayout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                enterButton1.setMaximumWidth(100)

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

        def createTabs(self, startDate, endDate):
            try:
                format = None
                if self.hourlyButton.isChecked():
                    dataDict = func.getHourly(startDate, endDate, self.peakHourStart.currentIndex(), self.peakHourStop.currentIndex())
                    dataString = func.dictStringHourly(dataDict)
                    format = "Hourly"
                elif self.dailyButton.isChecked():
                    dataDict = func.getDaily(startDate, endDate, self.peakHourStart.currentIndex(), self.peakHourStop.currentIndex())
                    dataString = func.dictString(dataDict)
                    format = "Daily"
                elif self.weeklyButton.isChecked():
                    dataDict = func.getWeekly(startDate, endDate, self.peakHourStart.currentIndex(), self.peakHourStop.currentIndex())
                    dataString = func.dictStringWeekly(dataDict)
                    format = "Weekly"
                elif self.monthlyButton.isChecked():
                    dataDict = func.getMonthly(startDate, endDate, self.peakHourStart.currentIndex(), self.peakHourStop.currentIndex())
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


            except Exception as e:
                s = str(e)
                excType, excObj, excTb = sys.exc_info()
                fname = os.path.split(excTb.tb_frame.f_code.co_filename)[1]
                # Create errorer message window
                errorBox = QMessageBox()
                if s == "list index out of range":
                    errorBox.setText(s + "\nDue to the goofy way in which Wyze groups their data,\nsame day start and end dates my return unexpected results\nor in this case, an error. Please try again with different dates.")
                    errorBox.exec()
                else:
                    errorBox.setText(s + "\n" + str(excType) + "\n" + fname + "\n" + str(excTb.tb_lineno))
                    errorBox.exec()
                print(sys.exc_info())

                self.errorLabel = QLabel(Exception.args[0])
                print(Exception.args[0])
                self.errorLabel.setFont(errorFont)
                self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.tab1.layout().addWidget(self.errorLabel)


        def removeTab(self, index):
            self.tabs.removeTab(index)

    class deviceListWindow(QWidget):
        def __init__(self, xCoord, yCoord):
            super().__init__()
            self.setWindowTitle("Wyze Data Portal - Device List")
            self.setGeometry(xCoord - 90, yCoord - 10, 600, 400)
            self.setContentsMargins(20, 20, 20, 20)
            self.setWindowIcon(QIcon('Widgets/WyzeLogo.PNG'))

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

            # Add Logo
            image = QLabel(self)
            pixmap = QPixmap('Widgets/WyzeLogo.PNG')
            scaled_pixmap = pixmap.scaled(150, 150)
            image.setPixmap(scaled_pixmap)
            logoHBox = QHBoxLayout()
            logoHBox.addWidget(image, alignment=Qt.AlignmentFlag.AlignCenter)
            rightLayout.addLayout(logoHBox)

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
            self.setWindowIcon(QIcon('Widgets/WyzeLogo.PNG'))

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

            image = QLabel(self)
            pixmap = QPixmap('Widgets/WyzeLogo.PNG')
            scaled_pixmap = pixmap.scaled(50, 50)
            image.setPixmap(scaled_pixmap)
            logoHBox = QHBoxLayout()
            logoHBox.addWidget(image, alignment=Qt.AlignmentFlag.AlignCenter)
            BottomLayout.addLayout(logoHBox)

            # Create discriptive link to Wyze API Key page
            hBox2 = QHBoxLayout()
            hBox2.addWidget(QLabel("You can generate a Wyze API key here:"), alignment=Qt.AlignmentFlag.AlignCenter)
            hBox3 = QHBoxLayout()
            wyzeLink = QLabel()
            wyzeLink.setOpenExternalLinks(True)
            wyzeLink.setTextFormat(Qt.TextFormat.RichText)
            wyzeLink.setText('<a href="https://developer-api-console.wyze.com/#/apikey/view">Wyze API Key</a>')
            wyzeLink.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hBox3.addWidget(wyzeLink)
            BottomLayout.addLayout(hBox2)
            BottomLayout.addLayout(hBox3)

            # Create another link for additional help
            hBox4 = QHBoxLayout()
            hBox4.addWidget(QLabel('You can find additional instructions here:'), alignment=Qt.AlignmentFlag.AlignCenter)
            hBox5 = QHBoxLayout()
            helpLink = QLabel()
            helpLink.setOpenExternalLinks(True)
            helpLink.setTextFormat(Qt.TextFormat.RichText)
            helpLink.setText('<a href="https://support.wyze.com/hc/en-us/articles/16129834216731-Creating-an-API-Key">Help</a>')
            helpLink.setAlignment(Qt.AlignmentFlag.AlignCenter)
            hBox5.addWidget(helpLink)

            BottomLayout.addSpacing(10)
            BottomLayout.addLayout(hBox4)
            BottomLayout.addLayout(hBox5)

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
            try:
                func.setClient(self.email.text(), self.password.text(), self.key_id.text(), self.api_key.text())
                xCoord = self.geometry().getCoords()[0]
                yCoord = self.geometry().getCoords()[1]
                self.deviceListWindow = deviceListWindow(xCoord, yCoord)
                self.deviceListWindow.show()
                #Seems to work, but I'm not sure if it's the best way to do it
                self.window().close()

            except WyzeApiError as e:
                s = str(e)
                print("Got Problems")
                print(s)
            
            except requests.exceptions.HTTPError as e:
                print("HTTP Error occurred:", e)
                print("Invalid credentials provided.")

                error_box = QMessageBox()
                error_box.setIcon(QMessageBox.Icon.Critical)
                error_box.setWindowTitle("Error")
                error_box.setText('Invalid Credentials')
                error_box.exec()
            
    def main():
        App=QApplication(sys.argv)
        window = Window()
        sys.exit(App.exec())

    if __name__=='__main__':
        main()


except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)



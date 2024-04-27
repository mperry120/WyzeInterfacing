import os
import func
import PyQt6

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
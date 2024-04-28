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
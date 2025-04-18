import os
import datetime
import pprint
from collections import defaultdict
from datetime import timedelta

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x450")

button1 = Button(root, text = 'Click for tiddies')
button2 = ttk.Button(root, text = 'Click for tiddies')
button1.pack()
button2.pack()


root.mainloop()

theDict = {
    datetime.datetime(2024, 4, 1, 1, 0, 0): 1,
    datetime.datetime(2024, 4, 1, 2, 0, 0): 2,
    datetime.datetime(2024, 4, 2, 1, 0, 0): 3,
    datetime.datetime(2024, 4, 2, 2, 0, 0): 4
}

newDict = defaultdict(int)

#make list
for date, value in theDict.items():
    day = date.date()
    newDict[day] += value

for key, value in newDict.items():
    string = key.strftime('%m/%d/%Y')
    print(string, ':', value)

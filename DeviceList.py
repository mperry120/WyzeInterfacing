import os
import datetime
import time
import calendar
import pprint
from collections import defaultdict
from datetime import timedelta
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError

leftPlugMac = '7C78B2647DD3-0002'
leftPlugModel = 'WLPPO-SUB'

client = Client(
    email = 'mperry120@gmail.com',
    password = 'ziJfym-fodsaq-ribwo6',
    key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')

def printDailyPowerUsage():
    #Print formatted daily usage list
    num = 0
    dateBuff = "None"
    dailyTotal = 0
    runningTotal = 0
    for x in keyList:
        date = keyList[num].strftime('%m/%d/%Y %H:%M:%S')
        if date[:10] != dateBuff[:10]:
            print("Total: ", dailyTotal / 1000)
            dailyTotal = 0
            print('=================\n')
            print(date[:10])
            print()
            print(date[11:16], "-- ", usageList[num] / 1000, "KWh")
            dailyTotal += usageList[num]
            runningTotal += usageList[num]
            
        else:
            print(date[11:16], "-- ", usageList[num] / 1000, "KWh")
            dailyTotal += usageList[num]
            runningTotal += usageList[num]

        num += 1
        dateBuff = date
    print("Total: ", dailyTotal / 1000, "KWh")
    print('=================')
    print("Comprehensive Total: ", runningTotal / 1000, "KWh")


def printDaily():
    num = 0
    for x in keyList:
        #make list
        theList = []


def testFunc():
    newDict = defaultdict(int)

    #make list
    for dict in PlugRecords:
        for date, value in dict.items():
            day = date.date()
            newDict[day] += value

        for key, value in dict.items():
            string = key.strftime('%m/%d/%Y')
            print(string, ':', value)

def printMonthlyPowerUsage():
    # Print formatted monthly usage list
    num = 0
    monthBuff = "None"
    dayBuff = "None"
    dailyTotal = 0
    monthlyTotal = 0
    runningTotal = 0
    for x in keyList:
        #change below code to:
        # month = x.strftime('%m/%Y')
        # day = x.strftime('%d')
        month = keyList[num].strftime('%m/%Y')
        day = keyList[num].strftime('%d')
        if month != monthBuff:
            if num != 0:
                print("Total: ", monthlyTotal / 1000)
            monthlyTotal = 0
            print('=================\n')
            print(month, day)
            print()
            if day != dayBuff:
                print(day, "- total(from new month): ", dailyTotal / 1000, "KWh")
                dailyTotal = 0
            monthlyTotal += usageList[num]
            runningTotal += usageList[num]
            dayBuff = day
        else:
            if day != dayBuff:
                print(day, "- total(from daily tally): ", dailyTotal / 1000, "KWh")
                dailyTotal = 0
            dailyTotal += usageList[num]
            monthlyTotal += usageList[num]
            runningTotal += usageList[num]
            dayBuff = day
        num += 1
        monthBuff = month
    print("Total: ", monthlyTotal / 1000, "KWh")
    print('=================')
    print("Comprehensive Total: ", runningTotal / 1000, "KWh")

def printHourlyPowerUsage():
    # Print formatted monthly usage list
    num = 0
    monthBuff = "None"
    monthlyTotal = 0
    runningTotal = 0
    for x in keyList:
        month = keyList[num].strftime('%m/%Y')
        if month != monthBuff:
            print("Total: ", monthlyTotal / 1000)
            monthlyTotal = 0
            print('=================\n')
            print(month)
            print()
            print(keyList[num].strftime('%m/%d/%Y %H:%M:%S'), "-- ", usageList[num] / 1000, "KWh")
            monthlyTotal += usageList[num]
            runningTotal += usageList[num]
        else:
            print(keyList[num].strftime('%m/%d/%Y %H:%M:%S'), "-- ", usageList[num] / 1000, "KWh")
            monthlyTotal += usageList[num]
            runningTotal += usageList[num]
        num += 1
        monthBuff = month
    print("Total: ", monthlyTotal / 1000, "KWh")
    print('=================')
    print("Comprehensive Total: ", runningTotal / 1000, "KWh")

try:
    # DeviceList = client.devices_list()
    # print("====================================\n")
    # for device in client.devices_list():
    #     print(f"mac: {device.mac}")
    #     print(f"nickname: {device.nickname}")
    #     print(f"is_online: {device.is_online}")
    #     print(f"product model: {device.product.model}")
    #     print()
    # print("\n====================================\n")


    # plug = client.plugs.info(device_mac='7C78B2647DD3-0002')
    # print("power: ", plug.is_on)
    # print("online: ", plug.is_online)

    # if plug.is_on:
    #     client.plugs.turn_off(device_mac=plug.mac, device_model=plug.product.model)
    #     print("Turned the plug off")
    # else:
    #     client.plugs.turn_on(device_mac=plug.mac, device_model=plug.product.model)
    #     print("Turned the plug on")
    # plug = client.plugs.info(device_mac='7C78B2647DD3-0002')
    # print(f"power: {plug.is_on}")


    leftPlug = client.plugs.info(device_mac='7C78B2647DD3-0001')
    
    #Querie for AC plug
    outdoorPlug = client.plugs.info(device_mac='7C78B2647DD3')


    #Assignes electrical usage records to "PlugRecords" Var
    PlugRecords = client.plugs.get_usage_records(device_mac=outdoorPlug.mac, device_model=outdoorPlug.product.model, start_time=datetime.datetime.fromisoformat('2024-03-31'))


    #Parse the PlugRecords dict
    keyList = []
    usageList = []
    cycle = 0
    for rec in PlugRecords:
        #cache PlugRecords keys
        #delete index
        index = 1
        keys = PlugRecords[cycle].hourly_data.keys()
        for key in keys:
            temp = [key]
            keyList += temp
            index += 1
        
        #cache PlugRecords values
        value = PlugRecords[cycle].hourly_data.values()
        for i in value:
            temp = [i]
            usageList += temp
        cycle += 1
        
    string = keyList[0].strftime('%m/%d/%Y %H:%M:%S')
    print(type(string))
    print(string)
    print(len(PlugRecords))
    printHourlyPowerUsage()
    printMonthlyPowerUsage()
    print("====================================\n") 
    for x in PlugRecords:
        print()
        pprint.pprint(x)
    
    print("-------------set--------------")
    testFunc()





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)



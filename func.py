from collections import defaultdict
import datetime
import wyze_sdk
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError


#Will need to create a setter function to pull all these values from the GUI
client = Client(
    email = 'mperry120@gmail.com',
    password = 'ziJfym-fodsaq-ribwo6',
    key_id ='0cf980f9-364e-44a5-9471-8ac8ec5fb6ff',
    api_key = 'XLMyd6F1Zs92SedNfGCrEs4a2l2oHnNwnMQx1YPxN9h2TZXR23gwz8avWYN7')

#Set global variables
outdoorPlug = None


#Querie for AC plug
def setPlugData(mac):
    global outdoorPlug
    outdoorPlug = client.plugs.info(device_mac= mac)
    

#Passes string literal date in the format of: 'YYYY-MM-DD'
def getUsageData(date):
    #Assignes electrical usage records to "PlugRecords" Var
    print(outdoorPlug.mac)
    PlugRecords = client.plugs.get_usage_records(device_mac=outdoorPlug.mac, device_model=outdoorPlug.product.model, start_time=datetime.datetime.fromisoformat(date))
    return PlugRecords

def printDaily(date):
    plugRecs = getUsageData(date)
    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            day = date.date()
            newDict[day] += value
    #print data
    for key, value in newDict.items():
        string = key.strftime('%m/%d/%Y')
        print(f"{string}:{value / 1000} KWh")
    #Create string
    rtrnString = ''
    monthParser = list(newDict.keys())
    month = monthParser[0].strftime('%m')
    rtrnString = monthParser[0].strftime('%B %Y') + '\n'
    for key, value in newDict.items():
        if key.strftime('%m') != month:
            rtrnString += (f"\n{key.strftime('%B %Y')}\n{key.strftime('%a the %d')}: {value / 1000} KWh\n")
            month = key.strftime('%m')
            print("from new line")
        else:
            rtrnString += (f"{key.strftime('%a the %d')}: {value / 1000} KWh\n")
            month = key.strftime('%m')
            print("from same line")
    return rtrnString


#TESTING

def printDailyString(date):
    plugRecs = getUsageData(date)
    newDict = defaultdict(int)
    rtrnString = ''
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            day = date.date()
            newDict[day] += value
    #print data
    for key, value in newDict.items():
        string = key.strftime('%m/%d/%Y')
        rtrnString += (f"{string}: {value / 1000} KWh\n")
    return rtrnString


#TESTING


def printMonthly(date):
    plugRecs = getUsageData(date)
    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            month_year = (date.year, date.month)
            newDict[month_year] += value
    #print data
    for key, value in newDict.items():
        year, month = key
        string = datetime.datetime(year, month, 1).strftime('%m/%Y')
        print(f"{string}:{value / 1000} KWh")





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

def getDeviceList():
    deviceListString = ""
    DeviceList = client.devices_list()
    print("====================================\n")
    for device in client.devices_list():
        deviceListString += (f"mac: {device.mac}\nnickname: {device.nickname}\nis_online: {device.is_online}\nproduct model: {device.product.model}\n")
        deviceListString += "\n ----- \n"
        print(f"mac: {device.mac}")
        print(f"nickname: {device.nickname}")
        print(f"is_online: {device.is_online}")
        print(f"product model: {device.product.model}")
        print()
    print("\n====================================\n")
    return deviceListString


# Need to pass in device_mac
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


#returns state of rememberMe last time user logged in
def get_rememberMe(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('rememberMe:'):
                rememberMe = line.split(':', 1)[1].strip()
                if rememberMe == 'true':
                    return True
                else:
                    return False
    return False

def get_email(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line starts with 'email:'
            if line.startswith('email:'):
                # Extract the email
                email = line.split(':', 1)[1].strip()
                return email
    # If 'email:' is not found in the file
    return None

def get_password(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('password:'):
                password = line.split(':', 1)[1].strip()
                return password
    return None

def get_key_id(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('key_id:'):
                key_id = line.split(':', 1)[1].strip()
                return key_id
    return None

def get_api_key(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('api_key:'):
                api_key = line.split(':', 1)[1].strip()
                return api_key
    return None
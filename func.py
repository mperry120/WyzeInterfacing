from collections import defaultdict
import datetime
import wyze_sdk
from wyze_sdk import Client
from wyze_sdk.errors import WyzeApiError
from dateutil.relativedelta import relativedelta, MO, SU
import calendar


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
    print('************************************')
    print(outdoorPlug)
    print('************************************')
    return outdoorPlug

    

#Passes string literal date in the format of: 'YYYY-MM-DD'
#NEED EXCEPTION HANDLING
def getUsageData(date):
    #Assignes electrical usage records to "PlugRecords" Var
    print(outdoorPlug.mac)
    PlugRecords = client.plugs.get_usage_records(device_mac=outdoorPlug.mac, device_model=outdoorPlug.product.model, start_time=datetime.datetime.fromisoformat(date))
    return PlugRecords

#Returns hourly usage dict of format: {datetime.datetime: int}
def getHourly(date, endDate):
    #changes
    startDate = datetime.datetime.strptime(date, '%Y-%m-%d')
    dayDelta = datetime.timedelta(days=1)
    pullDate = startDate - dayDelta
    sDate = startDate.replace(hour=0)
    
    tempDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    eDate = tempDate.replace(hour=23)
    
    #changes
    plugRecs = getUsageData(pullDate.strftime('%Y-%m-%d'))
    
    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            #changes
            if date <= eDate and date >= sDate:

                newDict[date] += value
    return newDict

#Returns daily usage dict of format: {datetime.date: int}
def getDaily(date, endDate):
    startDate = datetime.datetime.strptime(date, '%Y-%m-%d')
    dayDelta = datetime.timedelta(days=1)
    pullDate = startDate - dayDelta
    sDate = startDate.replace(hour=0)

    tempDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    eDate = tempDate.replace(hour=23)

    plugRecs = getUsageData(pullDate.strftime('%Y-%m-%d'))
                            
    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            if date <= eDate and date >= sDate:
                day = date.date()
                newDict[day] += value
    return newDict

#Returns weekly usage dict of format: {(datetime.date, datetime.date): int}
def getWeekly(date, endDate):
    startDate = datetime.datetime.strptime(date, '%Y-%m-%d')
    dayDelta = datetime.timedelta(days=1)
    pullDate = startDate - dayDelta
    sDate = startDate.replace(hour=0)

    tempDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    eDate = tempDate.replace(hour=23)

    plugRecs = getUsageData(pullDate.strftime('%Y-%m-%d'))

    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            if date <= eDate and date >= sDate:
                week = (date.year, date.date().isocalendar()[1])
                newDict[week] += value
    return newDict

def getMonthly(date, endDate):
    startDate = datetime.datetime.strptime(date, '%Y-%m-%d')
    dayDelta = datetime.timedelta(days=1)
    pullDate = startDate - dayDelta
    sDate = startDate.replace(hour=0)

    tempDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    eDate = tempDate.replace(hour=23)
    plugRecs = getUsageData(pullDate.strftime('%Y-%m-%d'))
    newDict = defaultdict(int)
    #make list
    for wyzeRec in plugRecs:
        #aggragate data
        for date, value in wyzeRec.hourly_data.items():
            if date <= eDate and date >= sDate:
                month = date.replace(day=1).replace(hour=0)
                newDict[month] += value
    return newDict

#Create string
def dictString(dict):
    rtrnString = ''
    monthParser = list(dict.keys())
    month = monthParser[0].strftime('%m')
    rtrnString = monthParser[0].strftime('%B %Y') + '\n'
    for key, value in dict.items():
        if key.strftime('%m') != month:
            rtrnString += (f"\n{key.strftime('%B %Y')}\n{key.strftime('%d %a'):8}- {value / 1000:>8} KWh\n")
            month = key.strftime('%m')
        else:
            rtrnString += (f"{key.strftime('%d %a'):8}- {value / 1000:>8} KWh\n")
            month = key.strftime('%m')
    return rtrnString.replace(' -', '--').replace('-     ', '------').replace('-    ', '-----').replace('-   ', '----')


#Create string for daily printout
def dictStringHourly(dict):
    rtrnString = ''
    monthParser = list(dict.keys())
    month = monthParser[0].strftime('%m')
    rtrnString = monthParser[0].strftime('%B %Y') + '\n'
    for key, value in dict.items():
        if key.strftime('%m') != month:
            rtrnString += (f"\n{key.strftime('%B %Y')}\n{key.strftime('%d %a %I%p'):10}- {value / 1000:>8} KWh\n")
            month = key.strftime('%m')
        else:
            rtrnString += (f"{key.strftime('%d %a %I%p'):12}- {value / 1000:>8} KWh\n")
            month = key.strftime('%m')
    
    return rtrnString.replace('-     ', '------').replace('-    ', '-----').replace('-   ', '----')

#Create string for weekly printout
def dictStringWeekly(dict):
    rtrnString = ''
    monthParser = list(dict.keys())
    #Get the first key in dict
    firstKey = list(monthParser[0])
    #Unpack the key into year and week
    year, week = firstKey
    #Convert year and week into a date
    firstDate = datetime.datetime.strptime(f'{year}-{week}-1', '%Y-%W-%w').date()

    month = firstDate.strftime('%m')
    rtrnString = firstDate.strftime('%B %Y') + '\n'
    for key, value in dict.items():
        year, week = key
        currentDate = datetime.datetime.strptime(f'{year}-{week}-1', '%Y-%W-%w').date()
        if currentDate.strftime('%m') != month:
            rtrnString += (f"\n{currentDate.strftime('%B %Y')}\n{formatWeek(year, week):<15}- {value / 1000:>8} KWh\n")
            month = currentDate.strftime('%m')
        else:
            rtrnString += (f"{formatWeek(year, week):<15}- {value / 1000:>8} KWh\n")
            month = currentDate.strftime('%m')
    
    return rtrnString.replace('-     ', '------').replace('-    ', '-----').replace('-   ', '----')

#Create string for monthly printout
def dictStringMonthly(dict):
    rtrnString = ''
    for key, value in dict.items():
        rtrnString += (f"{key.strftime('%B %Y'):8}- {value / 1000:>8} KWh\n")
    return rtrnString.replace('-     ', '------').replace('-    ', '-----').replace('-   ', '----')

#Create list from dict
def dictList(dict):
    list1 = []
    list2 = []
    for key, value in dict.items():
        if isinstance(key, datetime.date):
            list1 += [key]
            list2 += [float(value / 1000)]
        else:
            list1 += [key]
            list2 += [value]
    return list1, list2
    


def getDeviceList():
    deviceListString = ""
    DeviceList = client.devices_list()
    print("====================================\n")
    for device in client.devices_list():
        deviceListString += (f"nickname: {device.nickname}\nis_online: {device.is_online}\nmac: {device.mac}\nproduct model: {device.product.model}\n")
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

def get_last_mac(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('last_mac:'):
                Last_mac = line.split(':', 1)[1].strip()
                return Last_mac

def replaceLine(filename, oldLine, newLine):
    with open(filename, 'r') as file:
        data = file.read()
        if oldLine in data:
            for line in data.splitlines():
                if line.startswith(oldLine):
                    var1 = line.split(':', 1)[0].strip()
                    var2 = line.split(':', 1)[1].strip()
                    data = data.replace(var1 + ': ' + var2, var1 + ': ' + newLine)
            with open(filename, 'w') as file:
                file.write(data)
        else:
            data += newLine
            with open(filename, 'w') as file:
                data += '\n' + oldLine + newLine
                file.write(data)
            

def is_remembered(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('rememberMe:'):
                rememberMe = line.split(':', 1)[1].strip()
                if rememberMe == 'true':
                    return True
                else:
                    return False
                
def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def formatWeek(year, week):
    # Calculate the date of the Monday of the week
    mon = datetime.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()

    # Calculate the date of the Sunday of the week
    sun = mon + relativedelta(weekday=SU)

    # Format the dates into a string
    return f'MON {mon.day:>2} - SUN {sun.day:>2}'


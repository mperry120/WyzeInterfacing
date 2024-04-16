from collections import defaultdict
import datetime

theDict = {
    datetime.datetime(2024, 4, 1, 1, 0, 0): 1,
    datetime.datetime(2024, 4, 1, 2, 0, 0): 2,
    datetime.datetime(2024, 4, 2, 1, 0, 0): 3,
    datetime.datetime(2024, 4, 2, 2, 0, 0): 4
}

# Create a new dictionary to store the accumulated values for each day
newDict = defaultdict(int)

# Iterate through the original dictionary
for datetime_obj, value in theDict.items():
    # Extract the date part from the datetime object
    date_str = datetime_obj.date()
    # Increment the value for the corresponding date in the new dictionary
    newDict[date_str] += value

# Convert the defaultdict to a regular dictionary if needed
newDict = dict(newDict)

print(newDict)


    #Parse the PlugRecords dict
    # keyList = []
    # usageList = []
    # cycle = 0
    # for rec in PlugRecords:
    #     #cache PlugRecords keys
    #     #delete index
    #     index = 1
    #     keys = PlugRecords[cycle].hourly_data.keys()
    #     for key in keys:
    #         temp = [key]
    #         keyList += temp
    #         index += 1
        
    #     #cache PlugRecords values
    #     value = PlugRecords[cycle].hourly_data.values()
    #     for i in value:
    #         temp = [i]
    #         usageList += temp
    #     cycle += 1
        
    # string = keyList[0].strftime('%m/%d/%Y %H:%M:%S')
    # print(type(string))
    # print(string)
    # print(len(PlugRecords))
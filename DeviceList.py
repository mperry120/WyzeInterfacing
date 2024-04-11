import os
import datetime
import time
import calendar
import pprint
import func
from wyze_sdk.errors import WyzeApiError
from datetime import timedelta




leftPlugMac = '7C78B2647DD3-0002'
leftPlugModel = 'WLPPO-SUB'

pullDate = '2024-03-15'

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


    # leftPlug = client.plugs.info(device_mac='7C78B2647DD3-0001')
    
    





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

    print("-------------set--------------")
    func.printDaily(pullDate)
    func.printMonthly(pullDate)





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)





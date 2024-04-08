import os
import datetime
import time
import calendar
import pprint
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


    print("\n====================================\n")

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


    #Assignes electrical records to "PlugRecords" Var
    PlugRecords = client.plugs.get_usage_records(device_mac=outdoorPlug.mac, device_model=outdoorPlug.product.model, start_time=datetime.datetime.fromisoformat('2024-04-06'))

    print("\n====================================\n")

    pprint.pprint(PlugRecords[0].hourly_data)

    print("\n====================================\n")


    print("TESTING SECTION")
    print(list(PlugRecords[0].hourly_data.values()))
    print("TESTING SECTION")


    print("\n====================================\n")
    #Format and print PlugRecords
    i = 1
    for record in PlugRecords:
        print("Record ", i, ":")
        print(record.to_dict())
        print()
        i += 1
    print("\n====================================\n")

    print("Record type:")
    print(type(PlugRecords[0]))





except WyzeApiError as e:
    # You will get a WyzeApiError if the request failed
    print("power: ", plug.is_on)
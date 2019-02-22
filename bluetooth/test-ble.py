from network import Bluetooth
import pycom
import ubinascii
import os
import machine
import time


bluetooth = Bluetooth()
bluetooth.set_advertisement(name='Cow1',manufacturer_data='Team4', service_data='BLE')
bluetooth.advertise(True)
bluetooth.start_scan(-1)

def get_new_target_mac():
    """
    update the target MAC of the game
    """
    #-----------------------------------------------------------------------
    mac_list = list()
    device = bluetooth.get_adv()
    #-----------------------------------------------------------------------
    if (device is not None):
        device_mac  = str(ubinascii.hexlify(device.mac).decode())
        device_name = str(bluetooth.resolve_adv_data(device.data, Bluetooth.ADV_NAME_CMPL))
        devie_rssi  = str(device.rssi)
        #-----------------------------------------------------------------------
        current_target_mac = device_mac
        #-----------------------------------------------------------------------
        print('####################################')
        print (device_name + " " + device_mac + " " + devie_rssi)
        print(bluetooth.resolve_adv_data(device.data, Bluetooth.ADV_FLAG))
        print(bluetooth.resolve_adv_data(device.data, Bluetooth.ADV_NAME_CMPL))
        #-----------------------------------------------------------------------
        raw_mfg = bluetooth.resolve_adv_data(device.data, Bluetooth.ADV_MANUFACTURER_DATA)
        print(device_mac)
    else:
         print("no device")

def get_all_adv():
    mac_list=list()
    raw_macs=list()
    adv_list=bluetooth.get_advertisements()

    for device in adv_list:
        device_mac=str(ubinascii.hexlify(device.mac).decode())
        if device_mac in mac_list:
            pass
        else:
            raw_macs.append(device.mac)
            mac_list.append(device_mac)
            print("MAC: "+ device_mac)


#device_name=str(bluetooth.resolve_adv_data(device.Data, Bluetooth.ADV_NAME_CMPL))

#strength RSSI: str(device.RSSI)

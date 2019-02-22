import pycom
import network
from network import WLAN
from network import Bluetooth
from network import LoRa
import socket
import binascii
import math
import time
import gc
import machine
import uos
off = 0x000000
ESTIMOTE_SUBFRAMETYPE_A = 0
ESTIMOTE_SUBFRAMETYPE_B = 1
red = 0x330000
green = 0x003300
yellow = 0x333300
blue = 0x000033
purple = 0x330033
orange = 0x773300
white = 0x7f7f7f


def estimote_isTelemetry(pkt): # pkt=adv.data
    # Only accept an Estimote telemetry packet where UUID=0x9afe type=0x12
    if pkt[9]==0x9a and hex(pkt[10])=='0xfe' and hex(pkt[11])=='0x12':
        return(True)
    return(False)

def estimote_getBeaconIDRaw(pkt): # pkt=adv.data
    if estimote_isTelemetry(pkt):
        return(pkt[12:19])
    return(None)

def estimote_getBeaconID(pkt): # pkt=adv.data
    if estimote_isTelemetry(pkt):
        return(binascii.hexlify(pkt[12:19]))
    return(None)

def estimote_getSubframeType(pkt):
    return(pkt[20] & 0b00000011)

def estimote_getTemp(pkt):
    # Only available if this is a subframe B telemetry packet
    if (estimote_getSubframeType(pkt) != ESTIMOTE_SUBFRAMETYPE_B):
        return(None)
    #***** AMBIENT TEMPERATURE
    # upper 2 bits of byte 15[26] + byte 16[27] + lower 2 bits of byte 17[28
    # => ambient temperature RAW_VALUE, signed (two's complement) 12-bit integer
    # RAW_VALUE / 16.0 = ambient temperature in degrees Celsius
    tempRawValue = ((pkt[28] & 0b00000011) << 10) | (pkt[27] << 2) | ((pkt[26] & 0b11000000) >> 6)
    if tempRawValue > 2047:
      # way to convert an unsigned integer to a signed one (:
      tempRawValue = tempRawValue - 4096
    temp = tempRawValue / 16.0
    return(temp)

def estimote_getLight(pkt):
    # Only available if this is a subframe B telemetry packet
    if (estimote_getSubframeType(pkt) != ESTIMOTE_SUBFRAMETYPE_B):
        return(None)
    # ***** AMBIENT LIGHT
    # byte 13[24] => ambient light level RAW_VALUE
    # the RAW_VALUE byte is split into two halves
    # pow(2, RAW_VALUE_UPPER_HALF) * RAW_VALUE_LOWER_HALF * 0.72 = light level in lux (lx)
    ambientLightUpper = (pkt[24] & 0b11110000) >> 4
    ambientLightLower = pkt[24] & 0b00001111
    ambientLightLevel = math.pow(2, ambientLightUpper) * ambientLightLower * 0.72
    return(ambientLightLevel)

def ble_sweepEstimoteTempLight(ble, ids, duration=120, initColour=off):
    start = time.time()
    dataDict = {id: (start, 0, None, None) for id in ids}
    notSeenB = list(ids)
    threshold = 0
    telemCount = 0
    advCount = 0
    colour = initColour
    ble.start_scan(duration)
    while (ble.isscanning()):
        pycom.rgbled(colour)
        adv = ble.get_adv()
        now = time.time()
        if (adv):
            advCount = advCount + 1
            id = estimote_getBeaconID(adv.data)
            type = estimote_getSubframeType(adv.data)
            if (id in ids):
                telemCount = telemCount + 1
                (timeB, countB, temp, light) = dataDict[id]
                if (type==ESTIMOTE_SUBFRAMETYPE_B):
                    temp = estimote_getTemp(adv.data)
                    light = estimote_getLight(adv.data)
                    timeB = now
                    countB = countB + 1
                    if (id in notSeenB):
                        notSeenB.remove(id)
                    dataDict[id] = (timeB, countB, temp, light)
                    print("Beacon ", id, ": Temp=", temp, " Light=", light)
                if (len(notSeenB) == 0):
                    colour = blue
    if (ble.isscanning()):
        ble.stop_scan()
    pycom.rgbled(off)
    print('Advertisements:', advCount)
    print('Telemetry Pkts:', telemCount)

    if (len(notSeenB)>threshold):
        print('Missing beacons: ', notSeenB)
        return (None)

    return (dataDict)


def ble_get_estimotes(ble, duration=120):
    start = time.time()
    ids=[]
    rssi={}
    threshold = 0
    telemCount = 0
    advCount = 0
    ble.start_scan(duration)
    while (ble.isscanning()):
        adv = ble.get_adv()
        now = time.time()
        if (adv):
            #print (advCount)
            advCount = advCount + 1
            if estimote_getBeaconID(adv.data):
                id = estimote_getBeaconID(adv.data)
                if id not in ids:
                    ids.append(id)
                if id not in rssi:
                    rssi[id]=adv.rssi
                else:
                    rssi[id] = (rssi[id]+adv.rssi)/2
            #type = estimote_getSubframeType(adv.data)
    if (ble.isscanning()):
        ble.stop_scan()
    output =[]
    output.append(max(rssi, key=rssi.get))
    print('this is the valuse of output : ',output)
    print ('estimote IDs : ', str(ids))
    print('Advertisements:', advCount)
    print('Telemetry Pkts:', telemCount)
    print('indicated RSSI: ', rssi)
    return (output)

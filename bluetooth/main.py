# See https://docs.pycom.io for more information regarding library specifics
import pycom
import _thread
import time
import socket
import config
import lpwan
import struct
import estimote
from machine import WDT
from network import Bluetooth
from network import LoRa
from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE
from network import WLAN
wlan = WLAN()
wlan.deinit()

#Data encoder for signed integer values +/-32k
def enc_sigint(sample):
    sample = int(sample)
    flag = 0
    if sample < 0:
        flag = 128
        sample *= -1
    bigbits = int(sample/256)
    littlebits = sample - (bigbits*256)
    samplebytes = [(bigbits+flag),littlebits]
    tester = bytearray(samplebytes)
    return(tester)

## import device specific data from config file

app_eui = config.APP_EUI
app_key = config.APP_KEY
wifi_mac = config.WIFI_MAC
sys_info = config.SYS_INFO
ble = Bluetooth()
ids=[]
pycom.heartbeat(False)


## set LoRa mode and region

lora = LoRa(mode=LoRa.LORAWAN,region=LoRa.EU868)
## set LoRa MAC identifier
lora_mac = config.lora_mac(lora)

## WIFI setup

#wlan = WLAN(mode=WLAN.AP, ssid=lora_mac, auth=(WLAN.WPA2,'www.pycom.io'),
#            channel=7, antenna=WLAN.INT_ANT)

# Display our device info & address
print(sys_info)
print(lora_mac)


# join a network using OTAA
sfdr = 5
sfdr_min = 0 # SF12
sfdr_max = 5 # SF7

pycom.rgbled(0x7f7f00) # yellow

while not(lora.has_joined()):
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0, dr=sfdr)
    time.sleep(20)
    if not lora.has_joined() and sfdr !=0:
        sfdr -= 1
pycom.rgbled(0x007f00) # green

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate SF7=5 SF8=4 SF9=3 SF10=2 SF11=1 SF12=0
s.setsockopt(socket.SOL_LORA, socket.SO_CONFIRMED, True)

# make the socket non-blocking
s.setblocking(False)

pycom.heartbeat(False)

#wdt = WDT(timeout=360000)

ids = estimote.ble_get_estimotes(ble, duration=60)
print ('ids = ',ids)

while True:
    if lora.has_joined():
#        wdt.feed()
        temp = estimote.ble_sweepEstimoteTempLight(ble, ids,30)[ids[0]]
        estimote_temp = temp[2]
        estimote_light = temp[3]
        # configuring the data rate
        s.setsockopt(socket.SOL_LORA, socket.SO_DR, sfdr)
        s.setblocking(False)
        payload = bytearray()
        payload += enc_sigint(int(estimote_temp*100))
        payload += enc_sigint(int(estimote_light*100))
        print (payload)
        print (len(payload))
        try:
            s.send(payload)
        except:
            print("message send failure")
        if (sfdr <= sfdr_min):
            sfdr = sfdr_max
        else:
            sfdr = sfdr - 1
        print ("estimote temp: " + str (estimote_temp))
        print ("estimote light: " + str (estimote_light))

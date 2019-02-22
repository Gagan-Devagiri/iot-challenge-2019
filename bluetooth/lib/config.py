import binascii
import machine
import uos

WIFI_MAC = binascii.hexlify(machine.unique_id()).lower()
SYS_INFO = (uos.uname())

APP_EUI = binascii.unhexlify('hex_eui')
APP_KEY = binascii.unhexlify('hex_app_key')
IDS = [b'274ecb4b36dbd7']

def lora_mac(lora):
    return (binascii.hexlify(lora.mac()).upper().decode('utf-8'))

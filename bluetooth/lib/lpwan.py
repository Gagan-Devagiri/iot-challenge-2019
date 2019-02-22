###############################################################################
## Title: Lora functions for Pytrack tracker
## Author : Mark Strevens, Simon Chapple 
## Version : 0.03
## University of Edinburgh
###############################################################################

import socket
from math import ceil

def ttw1(payBytes, toa=0.0,  sf=7, bw=125, cr=5):
    if (toa == 0.0):
        PreSym = 8 # LoRaWAN EU has 8 preamble symbols
        LoRaWANBytes = 13 # Number of bytes for LoRaWAN header
        HeaderFlag = 1 # Has explicit header
        de = 0
        if (sf >= 11):
            de = 1
        Tsym = pow(2, sf) / (bw * 1000) * 1000
        Tpre = (PreSym+4.25)*Tsym # In milliseconds
        PaySym = 8+(max(ceil((8*(payBytes+LoRaWANBytes)-4*sf+28+16-20*(1-HeaderFlag))/(4*(sf-2*de)))*(cr),0))
        Tpay = PaySym * Tsym # In milliseconds
        toa = (Tpre + Tpay) / 1000.0 # Convert to seconds
    print('TOA: ' + str(toa) + ' seconds')
    ttw = toa * 99.0 # 1% duty cycle
    print('TTW: ' + str(ttw) + ' seconds to wait [1% duty cycle]')
    return(toa + ttw) # non-blocking requires us to add in TOA to our wait time!
    
def send(sock, msg, dr=5): # Returns time-to-wait before duty cycle permits sending next message
    sock.setsockopt(socket.SOL_LORA, socket.SO_DR, dr)
    sock.send(msg)
    return(ttw1(len(msg), sf=(12 -dr)))
    
def minify(val):
    """
    Takes a floating point value (designed for decimal minutes)
    and returns a bytes object that contains the uint32 representation
    of it
    """
    temp = int(val * 10000)
    print(temp)
    b = temp.to_bytes(4,'little')
    return bytes([b[3], b[2], b[1], b[0]])
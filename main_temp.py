from machine import I2C
import time
import sht31
i2c = I2C(0, I2C.MASTER, baudrate=100000)

s31=sht31.SHT31(i2c)


while(True):
    data = s31.get_temp_humi(celsius=True)
    print(data)
    time.sleep(1)

import machine
import utime
from amg88xx import AMG88XX
sda=machine.Pin(18)
scl=machine.Pin(19)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
sensor = AMG88XX(i2c)
while True:
    utime.sleep(1)
    sensor.refresh()
    print('\n')
    for row in range(8):
        print()
        for col in range(8):
            print('{:4d}'.format(sensor[row, col]), end='')
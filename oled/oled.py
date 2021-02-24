import machine
import utime
import ssd1306
sda=machine.Pin(18)
scl=machine.Pin(19)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
loop = 0
while True:
    utime.sleep(1)
    oled.fill(0)
    oled.text("Loop Count", 0, 0)
    oled.text(str(loop), 0, 10)
    oled.show()
    loop=loop+1
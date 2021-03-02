from servo import Servo
from machine import Pin
import utime
import _thread
led = Pin(25, Pin.OUT)
s1 = Servo(2) 
oneDegree = 8.5
global commanded
commanded = False

def blink_thread():
    global commanded
    while True:
        if commanded:
            commanded = False
            led.value(1)
            utime.sleep_ms(10)
            led.value(0)
        utime.sleep(0.1)

_thread.start_new_thread(blink_thread, ())

while True:
    s1.goto(0)
    commanded = True
    utime.sleep(1)
    #s1.goto(1024)
    #utime.sleep(1)
    #s1.goto(0)
    for i in range(120):
        commanded = True
        s1.goto(i*oneDegree) 
        utime.sleep_ms(25)
    utime.sleep(1)
 
    s1.goto(0)
    commanded = True

    utime.sleep(1)
    s1.goto(30*oneDegree)
    commanded = True
    utime.sleep(1)

    s1.goto(60*oneDegree)
    commanded = True
    utime.sleep(1)

    s1.goto(90*oneDegree)
    commanded = True
    utime.sleep(1)

    s1.goto(120*oneDegree)
    commanded = True
    utime.sleep(1)

"""
    for i in range(1024):
        s1.goto(i) 
        utime.sleep_ms(1)

    for i in range(1024):
        s1.goto(i) 
        utime.sleep_ms(1)
    for i in range(1024,0,-1):
        s1.goto(i)
        utime.sleep_ms(1)
  """      
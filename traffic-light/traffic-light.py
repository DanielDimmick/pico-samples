import machine
import _thread
import utime

global button_pressed
button_pressed = False

red_led = machine.Pin(15, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)

button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.1)

_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        red_led.value(1)
        for i in range(20):
            buzzer.value(1)
            utime.sleep(0.1)
            buzzer.value(0)
            utime.sleep(0.1)
        global button_pressed
        button_pressed =False
    red_led.value(1)
    utime.sleep(5)
    yellow_led.value(1)
    utime.sleep(2)
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(1)
    utime.sleep(5)
    green_led.value(0)
    yellow_led.value(1)
    utime.sleep(5)
    yellow_led.value(0)
# Import the libraries needed for pins, threading and time functions
import machine
import _thread
import utime

# Setup the global variable and its initial value
global button_pressed
button_pressed = False

# Define the LED pins
red_led = machine.Pin(15, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)
green_led = machine.Pin(13, machine.Pin.OUT)

# Define the buzzer and button pins
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

# Function to update the global button_pressed variable when the button is pressed
# This contains its own infinite loop that will be run on a seperate thread
def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        utime.sleep(0.1)

# Create a thread from the button_reader_thread() function
_thread.start_new_thread(button_reader_thread, ())

# Main loop
while True:
    # If the button was pressed the button_reader_thread will have changed the button_pressed variable to True
    if button_pressed == True:
        red_led.value(1)
        # Tap the pizo buzzer 20 times
        for i in range(20):
            buzzer.value(1)
            utime.sleep(0.1)
            buzzer.value(0)
            utime.sleep(0.1)

        # Then change the value of button_pressed to False so that we dont sound the pizo again on the next loop round
        # unless we have pressed the button again
        global button_pressed
        button_pressed =False
    
    # Normal traffic light behaviour 
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
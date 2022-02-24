from machine import ADC, Pin
import utime

vsys = ADC(29)              # reads the system input voltage
charging = Pin(24, Pin.IN)  # reading GP24 tells us whether or not USB power is connected 
conversion_factor = 2.55 * 3.3 / 65535

full_battery = 4.2                  # these are our reference voltages for a full/empty battery, in volts
empty_battery = 3.4                 # the values could vary by battery size/manufacturer so you might need to adjust them

while True:
    voltage = vsys.read_u16() * conversion_factor
    percentage = 100 * ((voltage - empty_battery) / (full_battery - empty_battery))
    if percentage > 100:
        percentage = 100.00

    print(voltage)
    
    utime.sleep(1)
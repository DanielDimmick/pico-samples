import machine
import uasyncio
import network
from lib.queue import Queue
from lib.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("12 Southern Hill", "CS1AG!0s")

async def connectionMonitor(q):
    while True:
        if wlan.isconnected():
            if q.empty():
                print(wlan.ifconfig())
                print("Setting connection state to True")
                await q.put(True)
        else:
           if q.empty():
                print("Setting connection state to False")
                await q.put(False) 
        await uasyncio.sleep_ms(500)

async def startClient(q):
    while True:
        if not q.empty():
            state = await q.get()
            if state:
                print("Starting MQTT Client")
                c = MQTTClient("pico", "192.168.1.95")
                c.connect()
                c.publish(b"mqtt/pico", b"hello from pico")
                c.disconnect()
            else:
                print("Stopping MQTT")
        await uasyncio.sleep_ms(5000)
                
async def readTemp(q):
    while True:
        sensor_temp = machine.ADC(4)
        conversion_factor = 3.3 / (65535)
        reading = sensor_temp.read_u16() * conversion_factor 
        temperature = 27 - (reading - 0.706)/0.001721
        #if q.empty():
        #    await q.put(temperature)
        #    print(temperature)
        await uasyncio.sleep_ms(2000)
                
async def main():
    connectedQueue = Queue()
    tempQueue = Queue()
    messageQueue = Queue()
    uasyncio.create_task(connectionMonitor(connectedQueue))
    uasyncio.create_task(startClient(connectedQueue))
    uasyncio.create_task(readTemp(tempQueue))

    while True:
        await uasyncio.sleep_ms(5)

uasyncio.run(main())

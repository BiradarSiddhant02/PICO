import time
from machine import Pin

p0 = Pin(0, Pin.OUT)
led = Pin(25, Pin.OUT)

def transmit():
        p0.toggle()
        led.toggle()
        time.sleep(1)
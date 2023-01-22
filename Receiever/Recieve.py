import machine

p0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)

def recieve():
    value = p0.value()
    if(value == False):
        led(False)                                         #type: ignore
    else:
        led(True)                                       #type: ignore                               
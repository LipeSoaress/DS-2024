import machine
import time

ma = machine.Pin(27, machine.Pin.OUT)
ca = machine.Pin(26, machine.Pin.OUT)
co = machine.Pin(25, machine.Pin.OUT)

while True:
    ma.value(1)
    time.sleep(5)
    ma.value(0)

    ca.value(1)
    time.sleep(1)
    ca.value(0)

    co.value(1)
    time.sleep(3)
    co.value(0)
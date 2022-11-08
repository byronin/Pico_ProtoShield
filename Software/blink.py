from time import sleep
from machine import Pin

led=Pin(22,Pin.OUT)

while(1):
    led.value(1)
    sleep(0.2)
    led.value(0)
    sleep(0.2)
    
    
    
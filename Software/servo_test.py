from time import sleep
from machine import Pin, I2C, ADC
from machine import PWM
from ssd1306 import SSD1306_I2C
from utime import sleep, ticks_ms
from random import randrange
from oled import Write, GFX
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import framebuf

servo1 = PWM(Pin(2))
servo2 = PWM(Pin(3))
servo3 = PWM(Pin(4))
servo4 = PWM(Pin(5))
servo5 = PWM(Pin(6))
servo6 = PWM(Pin(7))

i2c=I2C(1, scl = Pin(15), sda = Pin(14), freq = 400000)
global oled
oled = SSD1306_I2C(128, 64, i2c)
write15 = Write(oled, ubuntu_mono_15)
write20 = Write(oled, ubuntu_mono_20)
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00") 
write20.text("Ronin", 24, 15)
write15.text("github.com/byronin", 0, 40)   
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
oled.blit(fb, 77, 10)
oled.show()

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
servo4.freq(50)
servo5.freq(50)
servo6.freq(50)
led=Pin(22,Pin.OUT) 

deg = 0
flag = 0
def setServoCycle (position):
    position = position * 45
    position = position + 1000
    servo1.duty_u16(position)
    servo2.duty_u16(position)
    servo3.duty_u16(position)
    servo4.duty_u16(position)
    servo5.duty_u16(position)
    servo6.duty_u16(position)
   

while(1):
    setServoCycle(deg)
    if deg == 0:
        flag = 0
        led.value(0)
    if deg == 180:
        flag = 1
        led.value(1)
    if flag == 0:
        deg += 1
    else:
        deg -= 1
    
    sleep(0.01)

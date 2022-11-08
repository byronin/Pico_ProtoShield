from time import sleep
from machine import Pin
from machine import PWM
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import framebuf

i2c=I2C(1,sda=Pin(14), scl=Pin(15), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

button1 = Pin(10,Pin.IN,Pin.PULL_UP)
button2 = Pin(11,Pin.IN,Pin.PULL_UP)
button3 = Pin(20,Pin.IN,Pin.PULL_UP)
button4 = Pin(21,Pin.IN,Pin.PULL_UP)
button5 = Pin(28,Pin.IN,Pin.PULL_UP)

servo1 = PWM(Pin(2))
servo2 = PWM(Pin(3))
servo3 = PWM(Pin(4))
servo4 = PWM(Pin(5))

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
servo4.freq(50)

deg1 = 100
deg2 = 170
deg3 = 0
deg4 = 145
m_flag = 0

write15 = Write(oled, ubuntu_mono_15)
write20 = Write(oled, ubuntu_mono_20)
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00") 
write20.text("Ronin", 24, 15)
write15.text("github.com/byronin", 0, 40)   
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
oled.blit(fb, 77, 10)    
oled.show()
oled.fill(0)
sleep(3)

def setServoCycle (servo,position):
    position = position * 45
    position = position + 1000
    servo.duty_u16(position)
    #sleep(0.001)

while True:
    write20.text("Servo Deg", 15, 0)
    oled.text("Servo 1:", 0,25)
    oled.text(str(deg1),66,25)
    oled.text("Servo 2:", 0,35)
    oled.text(str(deg2),66,35)
    oled.text("Servo 3:", 0,45)
    oled.text(str(deg3),66,45)
    oled.text("Servo 4:", 0,55)
    oled.text(str(deg4),66,55)    
    oled.show()
    
    oled.fill(0)
    
    if button1.value() == 0:
        setServoCycle(servo1,deg1)
        deg1 += 2
        if deg1 > 180:
            deg1 = 180
            
    if button2.value() == 0:
        setServoCycle(servo3,deg3)
        setServoCycle(servo2,deg2)
        deg2 += 5
        if deg2 > 180:
            deg2 = 180
        deg3 -= 5
        if deg3 < 0:
            deg3 = 0
            
    if button3.value() == 0:
        setServoCycle(servo1,deg1)
        deg1 -= 2
        if deg1 < 0:
            deg1 = 0
            
    if button4.value() == 0:
        setServoCycle(servo3,deg3)
        setServoCycle(servo2,deg2)
        deg2 -= 5
        if deg2 < 0:
            deg2 = 0
        deg3 += 5
        if deg3 > 180:
            deg3 = 180    
            
    if button5.value() == 0:
        while button5.value() == 0:
            write20.text("Servo Deg", 15, 0)
            oled.text("Servo 1:", 0,25)
            oled.text(str(deg1),66,25)
            oled.text("Servo 2:", 0,35)
            oled.text(str(deg2),66,35)
            oled.text("Servo 3:", 0,45)
            oled.text(str(deg3),66,45)
            oled.text("Servo 4:", 0,55)
            oled.text(str(deg4),66,55)
            oled.show()
            oled.fill(0)
            setServoCycle(servo4,deg4)
            
            if m_flag == 0:
                deg4 += 5
                if deg4 > 150:
                    deg4 = 150
                    
            if m_flag == 1:
                deg4 -= 5
                if deg4 < 10:
                    deg4 = 10
                
        if m_flag == 0:
            m_flag = 1
        else:
            m_flag = 0


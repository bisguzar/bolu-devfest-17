import ssd1306
from machine import I2C, Pin
from dht import DHT22
from time import sleep

i2c = I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)

dht = DHT22(Pin(2))



def measure_realtime():
    dht.measure()
    sleep(0.2)
    dht.measure()

def term1():
    oled.fill(0)
    oled.text("GDG Bolu", 0,0)
    oled.text("Sicak", 0,10)
    oled.text("Kanlisin", 0,20)
    oled.text(":)", 0, 30)
    oled.show()


kontrol = False
def term2():
    global kontrol
    oled.fill(0)
    oled.text("Cok", 0,0)
    oled.text("Sicak", 0,10)
    oled.text("Kanlisin", 0,20)
    oled.text(":O", 0, 30)
    oled.show()
    if kontrol == False:
        oled.invert(1)
        kontrol = True
    else:
        oled.invert(0)
        kontrol = False

def uyari():
    oled.fill(0)
    oled.text("Lutfen", 0,0)
    oled.text("Sensore", 0,10)
    oled.text("Hohlayin", 0,20)
    oled.show()

while True:
    measure_realtime()
    print(dht.temperature())
    print("test")
    if 27 < dht.temperature() <32:
        term1()
    elif dht.temperature()> 32:
        term2()
    else:
        uyari()
    sleep(0.2)

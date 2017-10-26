import ssd1306
from machine import I2C, Pin
from dht import DHT22
from time import sleep

i2c = I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(64, 48, i2c)

dht = DHT22(Pin(2))

def display(temp):
    oled.fill(0)
    oled.text("Sicaklik:",0,0)
    oled.text(str(temp),0,10)
    oled.show()

while True:
    sleep(0.2)
    dht.measure()
    sleep(0.2)
    sicaklik = dht.temperature()
    display(sicaklik)
    print(sicaklik)

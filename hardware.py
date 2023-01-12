import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Adafruit_ADS1x15
import subprocess

class Display:
    def __init__(self):
        # Setup MQ-3 Sensor
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1
        # Raspberry Pi pin configuration:
        self.RST = None  # on the PiOLED this pin isnt used
        # Note the following are only used with SPI:
        self.DC = 23
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)# 128x64 display with hardware I2C:
        # Initialize library.
        self.disp.begin()
        self.clear_display()

        
    def clear_display(self):
        # Clear display.
        self.disp.clear()
        self.disp.display()

    def write_display(self,msg):
        width = self.disp.width
        height = self.disp.height
        self.image = Image.new('1', (width, height))
        self.draw = ImageDraw.Draw(image)
        #load Font
        self.font = ImageFont.truetype('PixelOperator8.ttf',16)
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0,0,width,height), outline=0, fill=0)
        #write in the middle of display
        self.draw.text((30, 23), str(msg),font=font, fill=255)
        self.disp.image(image)
        self.disp.display()
        time.sleep(.1)

    def breathalyzer_read(self):
        self.mq3reading = adc.read_adc(0, gain=GAIN)
        return self.mq3reading


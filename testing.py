
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Setup MQ-3 Sensor
from Adafruit_ADS1x15 import ADS1x15
ADS115 = 0x01
adc = ADS1x15(ic=ADS115)
GAIN = 4096
SPS = 250

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

#set timer for breathalyzer reading
timer_value = 10
highest_value = 0
# Load default font.
font = ImageFont.truetype('PixelOperator8.ttf',16)

while True:
    mq3reading = adc.read_adc(0, gain=GAIN, sps=SPS)
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    #if(highest_value < mq3reading or timer_value == 0):
    highest_value = mq3reading
    #    timer_value = 10
    #timer_value = timer_value - 1

    # Write two lines of text.
    
    draw.text((x+30, top+25), str(highest_value),font=font, fill=255)
    #draw.text((x, top+8),     str(CPU), font=font, fill=255)
    #draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
    #draw.text((x, top+25),    str(Disk),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)


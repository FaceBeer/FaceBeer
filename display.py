import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class Display:
    def __init__(self):
        # Define the Reset Pin
        oled_reset = digitalio.DigitalInOut(board.D4)
        self.BORDER = 5
        self.WIDTH = 128
        self.HEIGHT = 64 
        #For I2C
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, self.i2c, addr=0x3C, reset=oled_reset)
        # load Font
        self.font = ImageFont.truetype('PixelOperator8.ttf', 16)
        

    def clear_display(self):
        # Clear display.
        self.oled.fill(0)
        self.oled.show()

    def display_write(self,msg):
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (self.oled.width, self.oled.height))
        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)
        # Draw a white background
        draw.rectangle((0, 0, self.oled.width, self.oled.height), outline=255, fill=255)
        # Draw a smaller inner rectangle
        draw.rectangle((self.BORDER, self.BORDER, self.oled.width - self.BORDER - 1, self.oled.height - self.BORDER - 1),outline=0,fill=0,)
        # set the message
        (font_width, font_height) = self.font.getsize(msg)
        draw.msg((self.oled.width // 2 - font_width // 2, self.oled.height // 2 - font_height // 2),msg,font=self.font,fill=255,)
        #display
        self.oled.image(image)
        self.oled.show()
if __name__ == "__main__":
    display = Display()
    display.display_write("dickbutt")

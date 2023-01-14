import time

from picamera import PiCamera

from classify import Model
from sensors import Camera, Button, MQ3

button = Button()
hardware = Hardware()
MQ3 = MQ3()
while True:
    max = 0
    while button.get():
        print(MQ3.read())

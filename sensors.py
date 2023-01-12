import io
import time

from PIL import Image
from picamera import PiCamera
import numpy as np


class Camera:
    def __init__(self):
        self.camera = PiCamera
        self.img_width = 1920
        self.img_height = 1080

    def get_frame(self):
        stream = io.BytesIO()
        with self.camera() as camera:
            camera.resolution = (self.img_width, self.img_height)
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')

        stream.seek(0)
        img = Image.open(stream)
        return img

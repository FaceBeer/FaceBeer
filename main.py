from picamera import PiCamera

from classify import Model
from sensors import Camera

def main():
    camera = Camera()
    model = Model()
    img = camera.get_frame()
    name = model.predict(img)
    print(name)


if __name__ == "__main__":
    main()
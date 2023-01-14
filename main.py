from enum import Enum
import time

from picamera import PiCamera

from classify import Model
from sensors import Camera, Button


class State(Enum):
    INITIAL = 0
    SELFIE = 1
    ML = 2
    IDENTIFIED = 3
    BLOW = 4
    DONE = 5

class Session:
    def __init__(self):
        self.state = State.INITIAL
        self.displayed_text = ""
        self.image = None
        self.name = None

class Controller:
    def __init__(self, session):
        self.session = session
        self.button = Button()
        self.camera = Camera()
        self.model = Model()
        self.name = None
        time.sleep(2)

    def display_text(self, text):
        if self.session.displayed_text != text:
            # text not yet displayed
            # TODO: display text
            self.session.displayed_text = text

    def run(self):
        print("Starting main loop")
        while True:  # main loop for state machine
            if self.session.state == State.INITIAL:
                text = "FaceBeer\nPose and Press"
                self.display_text(text)
                if self.session.button.get():
                    print("Taking selfie")
                    # pressed, time to take the selfie
                    self.session.state = State.SELFIE
            elif self.session.state == State.SELFIE:
                text = "Say Cheese!"
                self.display_text(text)
                self.session.image = self.camera.get_frame()
                # image grabbed, time to process
                self.session.state = State.FACE
            elif self.session.state == State.ML:
                text = "Processing your face"
                self.display_text(text)

            elif self.session.state == State.IDENTIFIED:
                text = ""
            elif self.session.state == State.BLOW:
                text = ""
            elif self.session.state == State.DONE:
                text = ""
            else:
                print("ERROR OCCURRED")

def main():
    session = Session()
    controller = Controller(session)



if __name__ == "__main__":
    main()
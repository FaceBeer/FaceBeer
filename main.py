from enum import Enum
import time
from argparse import ArgumentParser

from picamera import PiCamera

from model import Model
from sensors import Camera, Button


class State(Enum):
    INITIAL = 0
    SELFIE = 1
    ML = 2
    IDENTIFIED = 3
    BLOW = 4
    DONE = 5


class Session:
    def __init__(self, threshold=0.75):
        self.state = State.INITIAL
        self.displayed_text = ""
        self.image = None
        self.name = None
        self.confidence = None
        self.guest_threshold = threshold
        self.reset_start_time = None


class Controller:
    def __init__(self, session: Session):
        self.sess = session
        self.button = Button()
        self.camera = Camera()
        self.model = Model()
        time.sleep(2)

    def display_text(self, text):
        if self.sess.displayed_text != text:
            # text not yet displayed
            # TODO: display text
            self.sess.displayed_text = text

    def run(self):
        print("Starting main loop")
        while True:  # main loop for state machine
            if self.sess.state == State.INITIAL:
                text = "FaceBeer\nPress for selfie"
                self.display_text(text)
                if self.sess.button.get():
                    print("Taking selfie")
                    # pressed, time to take the selfie
                    self.sess.state = State.SELFIE
            elif self.sess.state == State.SELFIE:
                text = "Say Cheese!"
                self.display_text(text)
                self.sess.image = self.camera.get_frame()
                # image grabbed, time to process
                self.sess.state = State.FACE
            elif self.sess.state == State.ML:
                text = "Processing your pic"
                self.display_text(text)
                self.sess.name, self.sess.confidence = self.model.predict(self.sess.image)
                if self.sess.confidence < self.sess.guest_threshold:
                    # uncertain about who this is, assume it's a "guest"
                    self.sess.name = "Guest"
                    self.sess.confidence = 1.0 - self.sess.confidence # if it's 60% emre, then it's 40% guest
                self.sess.reset_start_time = time.time()
                self.sess.state = State.IDENTIFIED
            elif self.sess.state == State.IDENTIFIED:
                text = f"{self.sess.name}?\nHold button and blow\nResetting in 5s"
                self.display_text(text)
                if not self.button.get() and time.time() - self.sess.reset_start_time > 5:
                    # user didn't press button in 5 seconds, assume model was wrong
                    self.sess.state = State.INITIAL
                elif self.button.get():
                    # button pressed, assume user is blowiung
                    self.sess.state = State.BLOW
            elif self.sess.state == State.BLOW:
                text = "Blow for 5s"
                self.display_text(text)

            elif self.sess.state == State.DONE:
                text = ""
            else:
                print("ERROR OCCURRED")


def main():
    parser = ArgumentParser()
    parser.add_argument("-t", "--threshold", default=0.75)
    args = parser.parse_args()
    threshold = args.threshold
    session = Session(threshold)
    controller = Controller(session)


if __name__ == "__main__":
    main()

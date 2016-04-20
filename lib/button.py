from detector import *
from event import *
import RPi.GPIO as GPIO
import time

class ButtonDetector(Detector):
    # TODO: Change this to a XML file
    GPIO_PIN = 27
    def __init__(self):
        Detector.__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def check_input(self):
        input_state = GPIO.input(GPIO_PIN)
        if input_state == False:
            print("RECEIVED INPUT")
            self.throw_event()

    @on_event
    def throw_event(self):
        return Event(1, 1, "input", False, time.time(), 10000, "PRESSED BUTTON")

    def run(self):
        while True:
            self.check_input()
            time.sleep(0.2)


import RPi.GPIO as GPIO

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.state = False

    def on(self):
        GPIO.output(self.pin, True)
        self.state = True

    def off(self):
        GPIO.output(self.pin, False)
        self.state = False

    def toggle(self):
        self.state = not self.state
        GPIO.output(self.pin, self.state)

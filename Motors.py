import random
import math
import time
import numpy as np
import RPi.GPIO as GPIO


class Motors:

    def __init__(self, pin1, pin2, pwm):

        self.pin1 = pin1
        self.pin2 = pin2
        self.pwm = pwm

        GPIO.setmode(GPIO.BOARD)  # declare settings
        GPIO.setwarnings(False)  # remove warnings

        # Set pins to outputs
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pwm, GPIO.OUT)

        print("Motors are live")

    def run_motors(self):
        GPIO.output(self.pin1, GPIO.HIGH) # Set AIN1 high
        GPIO.output(self.pin2, GPIO.LOW) # Set AIN2 Low
        GPIO.output(self.pwm, GPIO.HIGH) # Set PWM high

        print("Wheels should be spinning")

    def motors_off(self):
        GPIO.output(self.pin1, GPIO.LOW)  # Set AIN1 low
        GPIO.output(self.pin2, GPIO.LOW)  # Set AIN2 Low
        GPIO.output(self.pwm, GPIO.LOW)  # Set PWM low

        print("Wheels should be off")
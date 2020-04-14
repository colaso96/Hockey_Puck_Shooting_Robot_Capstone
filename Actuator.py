import random
import math
import time
import numpy as np
import RPi.GPIO as GPIO


class Actuator:

    def __init__(self, pin1, pin2, pwm):

        self.pin1 = pin1
        self.pin2 = pin2
        self.pwm = pwm

        GPIO.setmode(GPIO.BOARD) # declare settings
        GPIO.setwarnings(False) # remove warnings

        # Set pins to outputs
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pwm, GPIO.OUT)

        print("Actuator is live")

    def extend(self):
        GPIO.output(self.pin1, GPIO.LOW) # Set BIN1
        GPIO.output(self.pin2, GPIO.HIGH) # Set BIN2
        GPIO.output(self.pwm, GPIO.HIGH) # Set PWM

        print("Actuator Extend")

    def retract(self):
        GPIO.output(self.pin1, GPIO.HIGH)  # Set BIN1
        GPIO.output(self.pin2, GPIO.LOW)  # Set BIN2
        GPIO.output(self.pwm, GPIO.HIGH)  # Set PWM

        print("Actuator Retract")

    def cycle(self, sleep_time):
        self.extend()
        time.sleep(sleep_time)
        self.retract()
        time.sleep(sleep_time)

    def actuator_off(self):
        GPIO.output(self.pin1, GPIO.LOW)  # Set BIN1
        GPIO.output(self.pin2, GPIO.LOW)  # Set BIN2
        GPIO.output(self.pwm, GPIO.LOW)  # Set PWM

        print("Actuator Off")
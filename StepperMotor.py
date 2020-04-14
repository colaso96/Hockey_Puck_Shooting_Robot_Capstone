import random
import math
import time
import numpy as np
import RPi.GPIO as GPIO


class StepperMotor:

    # Initializes a stepper motor given
    # int: direction - GPIO pin to control direction
    # int: step - GPIO pin to control the step
    def __init__(self, direction, step, delay):
        self.DIR = direction  # Pin to control direction
        self.STEP = step  # Pin to control the pulses
        self.delay = delay #0.0208  # Pulse time

        GPIO.setmode(GPIO.BOARD)  # declare settings
        GPIO.setwarnings(False)  # remove warnings

        # Set pins to outputs
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)

        print("Stepper is live")

    # Method to spin the stepper motor
    # int: step_count - the number of steps to take
    # bool: direction - the direction (0 or 1)
    def spin(self, step_count, direction):
        GPIO.output(self.DIR, direction)  # This sets direction pin to 0 or 1
        print("Spinning ", step_count, " steps")
        # Pulses from 0 to step count
        for i in range(0, step_count):
            GPIO.output(self.STEP, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.STEP, GPIO.LOW)
            time.sleep(self.delay)

    def stepper_off(self):
        print("Stepper off")
        GPIO.cleanup()

    def test_stepper(self):
        stepper.spin(50, 0)
        time.sleep(1)
        stepper.spin(50, 1)
        time.sleep(1)
        stepper.stepper_off()
    
#stepper = StepperMotor(38, 40)
#stepper.test_stepper()
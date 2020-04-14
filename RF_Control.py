import random
import math
import time
import numpy as np
import RPi.GPIO as GPIO
from lidar_lite import Lidar_Lite
from Motors import Motors
from StepperMotor import StepperMotor
from Actuator import Actuator


GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print(GPIO.input(37))

GPIO.add_event_detect(37, GPIO.RISING)

def my_callback(self):
    print("This shit is working!")

GPIO.add_event_callback(37, my_callback)



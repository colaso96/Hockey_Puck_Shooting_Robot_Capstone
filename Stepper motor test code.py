import random
import math
import time
import numpy as np
import RPi.GPIO as GPIO

class Trigger():
    
    def __init__(self):
        GPIO.setwarnings(False)
        print("Hello")
    
    def StepperMotor1Left(self):
        DIR = 38 # Direction GPIOPin
        STEP = 40 # STEP GPIO Pin
        CW = 1 # Clockwise Rotation
        CCW = 0 # Counterclockwise Rotation
        SPR = 25 
        
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CCW)
        
        step_count = SPR
        delay = 0.0208
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)
        GPIO.output(DIR, CW)
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)    

        
    def StepperMotor1Right(self):
        DIR = 38 # Direction GPIOPin
        STEP = 40 # STEP GPIO Pin
        CW = 1 # Clockwise Rotation
        CCW = 0 # Counterclockwise Rotation
        SPR = 25 
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CW)
        
        step_count = SPR
        delay = 0.0208
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)
        GPIO.output(DIR, CCW)
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)    

    
    def StepperMotor2Low(self):
        DIR = 38 # Direction GPIOPin
        STEP = 40 # STEP GPIO Pin
        CW = 1 # Clockwise Rotation
        CCW = 0 # Counterclockwise Rotation
        SPR = 25 
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CCW)
        
        step_count = SPR
        delay = 0.0208
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)
        GPIO.output(DIR, CW)
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)
        GPIO.cleanup()

        
    def StepperMotor2High(self):
        DIR = 38 # Direction GPIOPin
        STEP = 40 # STEP GPIO Pin
        CW = 1 # Clockwise Rotation
        CCW = 0 # Counterclockwise Rotation
        SPR = 25 
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)
        GPIO.output(DIR, CCW)
        
        step_count = SPR
        delay = 0.0208

        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(delay)
            
        time.sleep(.5)
        GPIO.output(DIR, CW)
        
        for x in range(step_count):
            GPIO.output(STEP, GPIO.HIGH) 
            time.sleep(delay)
            GPIO.output(STEP, GPIO.LOW)     
            time.sleep(delay)
            
        time.sleep(.5)    
        print ("stepper run")


#Setup Motor
Trigger1 = Trigger()
Trigger1.StepperMotor2High()


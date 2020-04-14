import random
import math
import time
import sys
import numpy as np
import RPi.GPIO as GPIO
from lidar_lite import Lidar_Lite
from Motors import Motors
from StepperMotor import StepperMotor
from Actuator import Actuator




# A class for the entire puck-shooting system
class System:

    # Constructor that takes in the number of pucks in the hopper
    def __init__(self, pucks):

        self.pucks = pucks
        self.current_x = 0  # the starting x position of the shooter
        self.current_y = 0  # the starting y position of the shooter
        self.lidar = Lidar_Lite()
        self.connected = self.lidar.connect(1)

        if self.connected < -1:
            print("Not Connected")
        else:
            print("Connected")

        self.distance = 15 #self.get_distance(2)  # distance from the goal
        self.theta_steps = self.get_vertical_steps()  # number of steps to hit cross bar (vertical)
        self.phi_steps = self.get_horizontal_steps()  # number of steps to hit post from center (horizontal)
        self.motors = Motors(31, 29, 33)  # DC Motors and the GPIO/PWM pins
        self.actuator = Actuator(16, 18, 32)  # Actuator and the GPIO/PWM pins
        self.horiz_stepper = StepperMotor(11, 13, 0.0208)  # Stepper motor to control horizontal motion, GPIO pins and time delay
        self.vert_stepper = StepperMotor(38, 40, 0.0208/5)  # Stepper motors to control verical motion, GPIO pins and time delay 

    # Returns the distance in feet from the lidar
    #@staticmethod
    def get_distance(self, threshold):
        lidar_reading = []
        number_list = []

        for i in range(0, 100):
            distance = self.lidar.getDistance()
            lidar_reading.append(distance)

        m = np.mean(lidar_reading)
        s = np.std(lidar_reading)

        for x in lidar_reading:
            if (x < (m + (threshold * s))) and (x > (m - (threshold * s))):
                number_list.append(x)
        print("distance is", np.mean(number_list) / 30.48)
        
        return np.mean(number_list) / 30.48  # converts from cm to ft? I think

    # Returns the vertical steps as an int
    def get_vertical_steps(self):
        net_height = 4   # Height of the net in feet
        theta = math.atan(net_height / self.distance)  # Desired launch angle
        print("theta is ", theta)
        ft_per_spin = 0.31875/12  # number of feet that the stepper rises with each full rotation
        radius_base = 2  # from rear pivot to lead screw in feet
        height_base = 4 / 12  # from ground to base in feet
        sigma = math.atan(height_base / radius_base)
        screw_length = radius_base**2 + (radius_base**2 + height_base**2) - (2 * radius_base *
            math.sqrt(radius_base**2 + height_base**2) * math.cos(theta + sigma))
        print("screw length is ", screw_length)
        spins = (screw_length - height_base) / ft_per_spin
        print("vetical step count is", (spins * 360)/1.8)
        
        return int((spins * 360) / 1.8)  # number of steps to hit crossbar

    # Returns the horizontal steps as an int
    def get_horizontal_steps(self):
        center_to_post = 3  # distance from center of net to a post
        phi = math.atan(center_to_post / self.distance)  # Desired rotation angle
        print("horizontal step count is", (phi * 57.2958) / 1.8)
        
        return int((phi * 57.2958) / 1.8)  # number of steps to hit post

    # Fires all of the pucks
    def fire_pucks(self):
        self.motors.run_motors()
        
        for x in range(1, self.pucks+1):
            hole = random.randint(1, 5)
            print(x, "puck shot, ", hole, " hole")
            self.aim(hole)
            time.sleep(0.5)
            self.actuator.cycle(1.6)  # cycle actuator using 1.6s sleep time
            
        
        self.motors.motors_off()
        self.actuator.actuator_off()
        self.horiz_stepper.stepper_off()
        self.vert_stepper.stepper_off()

    # Aims at the desired hole
    def aim(self, hole):
     
        if hole == 1:
            x = -1
            y = 0
        elif hole == 2:
            x = -1
            y = 1
        elif hole == 3:
            x = 1
            y = 1
        elif hole == 4:
            x = 1
            y = 0
        elif hole == 5:
            x = 0
            y = 0

        x_steps = x - self.current_x
        y_steps = y - self.current_y

        if x_steps < 0:
            x_dir = 0
        else:
            x_dir = 1

        if y_steps < 0:
            y_dir = 0
        else:
            y_dir = 1

        x_steps = int(abs(x_steps) * self.phi_steps)
        y_steps = int(abs(y_steps) * self.theta_steps)
        
        self.horiz_stepper.spin(x_steps, x_dir)
        self.vert_stepper.spin(y_steps, y_dir)

        self.current_x = x
        self.current_y = y
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN)#, pull_up_down=GPIO.PUD_DOWN)

print("37 is: ",GPIO.input(37))

def on_off(self):
    shooter = System(10)
    
    if GPIO.input(37):
        print("This shit is working!")  
        shooter.fire_pucks()
    
    else:
        print("off")
        shooter.motors.motors_off()
        shooter.actuator.actuator_off()
        shooter.horiz_stepper.stepper_off()
        shooter.vert_stepper.stepper_off()

        sys.exit()
    
GPIO.add_event_detect(37, GPIO.BOTH, callback = on_off)


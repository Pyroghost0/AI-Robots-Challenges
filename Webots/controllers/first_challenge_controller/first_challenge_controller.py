from controller import Robot
from controller import Motor
import math


# High level functions
def move_forward(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(max_speed)

def move_back():
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(-max_speed)

def turn_left(): 
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(max_speed)


def turn_right(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(-max_speed)


def reset_motors():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    camera_motor.setVelocity(0)
    
#Main    
if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    
    #Variables
    time_step = 64
    max_speed = .5
    max_camera_speed = 2.0

    #Set up motor/track wheels
    left_motor = robot.getDevice("leftMotor")
    right_motor = robot.getDevice("rightMotor")
    left_motor.setPosition(math.inf)
    right_motor.setPosition(math.inf)

    #Set up touch sensors
    left_sensor = robot.getDevice("left sensor")
    right_sensor = robot.getDevice("right sensor")
    left_sensor.enable(time_step)
    right_sensor.enable(time_step)

    #Set up camera and camera motor
    camera = robot.getDevice("camera")
    camera.enable(time_step)
    camera_motor = robot.getDevice("camera motor")
    camera_motor.setPosition(math.inf)
    camera_motor.setVelocity(0.0)
    reset_motors()

    #Local variables
    width = camera.getWidth()
    height = camera.getWidth()
    
    #Robot AI goes here **************
    move_forward()
    robot.step(time_step)
    
    #End of AI
    
    reset_motors()
    del robot
    pass  # EXIT_SUCCESS
    
    
    
    
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
    
#Main    
if __name__ == "__main__":
    # create the Robot instance.
    robot = Robot()
    
    #Variables
    time_step = 64
    max_speed = .35

    #Set up motor/track wheels
    left_motor = robot.getDevice("left_motor")
    right_motor = robot.getDevice("right_motor")
    left_motor.setPosition(math.inf)
    right_motor.setPosition(math.inf)

    reset_motors()
    
    #Robot AI goes here **************
    move_forward()
    robot.step(time_step)
    
    #End of AI
    
    reset_motors()
    del robot
    pass  # EXIT_SUCCESS
    
    
    
    
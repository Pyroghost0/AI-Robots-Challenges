

from controller import Robot
from controller import Motor
from controller import Keyboard
import math


# High level functions
#def move_forward(): 
#    left_motor.setVelocity(max_speed)
#    right_motor.setVelocity(max_speed)

def move_back():
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(-max_speed)

def turn_left(): 
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(max_speed)


def turn_right(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(-max_speed)


#def drive_forward(angle, inRadians = False): 
#    if inRadians: 
#        angle *= 57.295   #//180/3.14 = 57
#    if angle > 90 or angle < -90:
#        pass
#    elif angle >= 0:
#        left_motor.setVelocity(max_speed)
#        right_motor.setVelocity( max_speed * math.sin((angle + 45) / 28.648) )
#    else:
#        left_motor.setVelocity(max_speed * math.sin((-angle + 45) / 28.648) )
#    right_motor.setVelocity(max_speed)

def turn_camera_up():
    camera_motor.setVelocity(-max_camera_speed)

def turn_camera_down():
    camera_motor.setVelocity(max_camera_speed)

def reset_motors():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    camera_motor.setVelocity(0)


if __name__ == "__main__":
    #Create the Robot instance.
    robot = Robot()
    
    #Variables
    time_step = 64
    max_speed = 6.26
    max_camera_speed = 2.0
    camera_min_position = -1 #actually highest
    camera_max_position = 0.1 #actually lowest
    #speed of camera motor with auto ai 
    camera_auto_speed = 0.02 
    camera_default_position = 0
    camera_position = 0.0
    #variable if want camera going through ai or manual movement
    camera_manual = bool()
    camera_auto_direction = int()
    
    #Keyboard interaction instance
    keyboard = Keyboard()
    keyboard.enable(time_step)

    #Set up camera and camera motor
    camera = robot.getDevice("camera")
    camera.enable(time_step)
    
    #RotationalMotor Object initialization
    camera_motor = robot.getDevice("camera_motor_object")
    #print(type(camera_motor)) #Double check that object is a motor
    
    #Setting maximum rotational values of camera motor
    camera_motor.maxPosition = camera_max_position
    camera_motor.minPosition = camera_min_position
    
    #Main Loop while simulation is running
    while robot.step(time_step) != -1:
        #Get keyboard input every frame
        key = keyboard.getKey()
        
        if camera_manual != False and camera_manual != True:
            camera_manual = True
               
        #checks if either up/down arrow is pressed and applies position accordingly
        #using right arrow resets the camera to its default position 
        #using left arrow puts camera off of manual movement by flipping boolean value 
        #up arrow - Highest position
        if (key==315):
            print("[ Up Arrow    [^] ] pressed: Moving Camera to Max upwards position: " + str(camera_min_position))
            camera_manual = False
            camera_auto_direction = 1
            camera_position = camera_min_position #Highest position
        #down arrow - Lowest position
        elif (key==317):
            print("[ Down Arrow  [v] ] pressed: Moving Camera to Max downwards position: " + str(camera_max_position))
            camera_manual = False
            camera_auto_direction = 1
            camera_position = camera_max_position #Lowest position
        #right arrow key resets position to 0
        elif (key==316):
            print("[ Right Arrow [>] ] pressed: Moving Camera to default position: " + str(camera_default_position))
            camera_manual = False
            camera_auto_direction = 1
            camera_position = camera_default_position #default camera position
        #left arrow key makes it go through range of positions
        elif (key==314):
            print("[ Left Arrow  [<] ] pressed: Camera resuming AI Movement...")
            if camera_auto_direction != 1 and camera_auto_direction != -1:
                camera_auto_direction = 1 
            camera_manual = True
        
        #change behavior if user is controlling or not
        if(camera_manual == False): #user input mode
            #Change camera position based on last input    
            camera_motor.setPosition(camera_position)
        else: #Camera AI movement mode
            #To change with further implementation of camera code
            #Currently showing basic functionality
            if(camera_position <= camera_min_position): #if up all the way, go down
                #Changes movement to downwards
                #print("Camera now going down")
                camera_auto_direction = -1
                    
            elif(camera_position >= camera_max_position): #can go higher, go up
                #print("Camera now going up")
                camera_auto_direction = 1
                
            #change camera position
            camera_position -= (camera_auto_speed * camera_auto_direction)
            camera_motor.setPosition(camera_position)
                    
                
        
        
    
    #End of AI
    #reset_motors()
    #del robot
    pass  # EXIT_SUCCESS
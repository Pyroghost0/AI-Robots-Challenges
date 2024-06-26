#Resources
#https://cyberbotics.com/doc/guide/tutorial-8-the-supervisor?tab-language=python
#https://www.cyberbotics.com/doc/reference/supervisor?tab-language=python
from controller import Supervisor
import random
import math

#Max range of the distance objects move
MAX_RANGE = 0.01

#Creates supercisor instance of robot
#The robot itself must have the supervisor value set to true (default false)
robot = Supervisor()

robot.step(64)

#Start randomising placement
i = 0;
while True:
    #Gets node with definition ex. "Random_0"
    #Set a DEF by clicking on an object and editing DEF field (Not child node)
    node = robot.getFromDef('Random_' + str(i))
    if node is None:
        break;
        #print("No DEF node found in the current world file\n")
        #sys.exit(1)
    translation_field = node.getField('translation')
    #translation_field = robot.getSelf().getField('translation')
    
    #Randomises the position by placing offsetting it...
    #in radius with higher chance being in center
    position = node.getPosition();
    angle = random.uniform(0.0, 6.28318530718)
    distance = math.pow(random.uniform(0.0, 1.0), 2) * MAX_RANGE
    
    #Sets value and incliments to next random node
    new_value = [math.sin(angle) * distance + position[0], 
    math.cos(angle) * distance + position[1], position[2]]
    translation_field.setSFVec3f(new_value)
    node.resetPhysics()
    i+=1

node = robot.getFromDef('Random_0')
if node.getField('customData').getSFString() == 'true' or node.getField('customData').getSFString() == 'True':
    type = robot.getName()
    
    if type[0] == '1':#Track
        translation_field = node.getField('translation')
        translation_field.setSFVec3f([-.45, 0.0, node.getPosition()[2]])
        node.resetPhysics()
        
        node = robot.getFromDef('Duck')
        translation_field = node.getField('translation')
        
        angle = random.uniform(-1.15, 4.2)
        position = [math.sin(angle) * 0.44, 
        math.cos(angle) * 0.44, node.getPosition()[2]]

        translation_field.setSFVec3f(position)
        
        rotation_field = node.getField('rotation')
        rotation_field.setSFRotation([0.0, 0.0, 1.0, random.uniform(0.0, 6.28318530718)])
        
        node.resetPhysics()
        
    elif type[0] == '2':#All
        i = 1
        angles = []
        distances = []
        while True:
            node = robot.getFromDef('Random_' + str(i))
            if node is None:
                break;
            
            translation_field = node.getField('translation')
            
            angle = 0.0
            distance = 0.0
            position = [0.0, 0.0, 0.0]
            while True:
                angle = random.uniform(0.0, 6.28318530718)
                distance = random.uniform(0.15, 0.35)
                position = [math.sin(angle) * distance, 
                math.cos(angle) * distance, node.getPosition()[2]]
                
                safe = True
                j = 0
                while j < len(angles):
                    direction = [math.sin(angles[j]) * distances[j] - position[0], 
                    math.cos(angles[j]) * distances[j] - position[1]]
                    
                    if pow(pow(direction[0], 2) + pow(direction[1], 2), 0.5) < 0.1:
                        safe = False
                        break
                    j+=1
                if safe:
                    break
            
            angles.append(angle)
            distances.append(distance)
            translation_field.setSFVec3f(position)
            
            rotation_field = node.getField('rotation')
            rotation_field.setSFRotation([0.0, 0.0, 1.0, random.uniform(0.0, 6.28318530718)])
            
            node.resetPhysics()
            i+=1
    else:#Duck
        node = robot.getFromDef('Random_' + str(i-1))
        translation_field = node.getField('translation')
        
        position = [.15, 0.0, node.getPosition()[2]];
        angle = random.uniform(0.0, 3.14159265358)#Spawn in half circle
        distance = random.uniform(0.0, 1.0)
        
        #Sets value and incliments to next random node
        new_value = [math.sin(angle) * distance * .25 + position[0], 
        math.cos(angle) * distance * .38 + position[1], position[2]]
        translation_field.setSFVec3f(new_value)
        rotation_field = node.getField('rotation')
        rotation_field.setSFRotation([0.0, 0.0, 1.0, random.uniform(0.0, 6.28318530718)])
        node.resetPhysics()

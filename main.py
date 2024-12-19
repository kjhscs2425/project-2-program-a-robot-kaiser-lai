# Import the robot control commands from the library
from simulator import robot
import time


def f (distance):
    robot.motors(1 ,1, distance)
    return 1

def b (distance):
    robot.motors(-1, -1, distance)

def l (distance):
    robot.motors(1, -1, distance)

def r (distance):
    robot.motors(-1, 1, distance)

def s ():
    right, left = robot.sonars()
    print(left, right)
    if left < 150 or right < 150:
        print ('KYS: keep yourself safe')
    else:
        b(user)
        print('you are safe!!!!!')
    return left, right 
    
    
     
while True:
    going = input(" do you wish to continue y/n?").lower()
    if going == "y":
        user = float(input("how long u want to move?"))
        if user < 2:
            print("invalid input")
        turn = float(input("how long u want to turn?"))
        if turn < 2:
            print("invalid input")
        else:
            print("moving!")
            x = f(user)
            b(user)
            f(user)
            b(user)
            f(user)
            r(turn)
            l(turn)
            r(turn)
            l(turn)
            b(user)
            s()

    
    elif going == "n":
        robot.exit()
    else:
       print("speak human")

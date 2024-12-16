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
    if left < 100 or right < 100:
        print ('KYS: keep yourself safe')
    return left, right


while True:
    going = input(" do you wish to continue y/n?").lower()
    if going == "y":
        user = bool(input("how long u want to move?"))
        if user > 1<x<2:
            print("invalid input")
        else:
            print("moving!")
            x = f(user)
            r(3)
            b(user)
            l(3)
            s()
    
    elif going == "n":
        robot.exit()
    else:
       print("speak human")
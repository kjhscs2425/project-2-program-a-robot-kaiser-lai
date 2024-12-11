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
    return left, right


while True:
    exit = input(" do you wish to continue y/n?")
    if exit == "y":

        user = int(input("how long u want to move?"))

        f(user)
        r(4)
        l(4)
        b(user)
        left, right = s()
    elif exit == "n":
        robot.exit()
    else:
        print("speak human")
    


    




    



    



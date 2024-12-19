# Import the robot control commands from the library
from simulator import robot
import time

# Define movement functions
def forward(distance):
    robot.motors(1, 1, distance)
    return distance

def backward(distance):
    robot.motors(-1, -1, distance)

def turn_left(distance):
    robot.motors(1, -1, distance)

def turn_right(distance):
    robot.motors(-1, 1, distance)

def read_sonars():
    left, right = robot.sonars()
    print(f"Sonar Readings - Left: {left}, Right: {right}")
    return left, right

# Safe movement to prevent crashing into walls
def safe_move(distance):
    left, right = read_sonars()
    if left < 100 or right < 100:  # Threshold for wall detection
        print("Obstacle detected! Movement stopped.")
        return False
    forward(distance)
    return True

# Autonomous mode for 20 seconds
def autonomous_mode():
    print("Autonomous mode activated! The robot will move for 20 seconds.")
    start_time = time.time()
    while time.time() - start_time < 20:
        left, right = read_sonars()
        if left < 100 or right < 100:
            print("Obstacle detected! Avoiding...")
            backward(1)
            turn_left(1)
        else:
            forward(1)
            time.sleep(1)
    print("Exiting autonomous mode.")

# Remote control using WASD keys
def remote_control():
    print("Remote control activated! Use 'w', 'a', 's', 'd' to move and 'q' to quit.")
    while True:
        command = input("Enter a command (w/a/s/d/q): ").lower()
        if command == 'w':
            print("Moving forward!")
            safe_move(1)
        elif command == 's':
            print("Moving backward!")
            backward(1)
        elif command == 'a':
            print("Turning left!")
            turn_left(1)
        elif command == 'd':
            print("Turning right!")
            turn_right(1)
        elif command == 'q':
            print("Exiting remote control.")
            break
        else:
            print("Invalid command! Use 'w', 'a', 's', 'd', or 'q'.")

# Main control loop
def main():
    print("Welcome to the Robot Controller!")
    while True:
        user_input = input("\nEnter a command ('y' to control, 'n' to exit, 'auto' for autonomous mode, 'remote' for remote control): ").lower()

        if user_input == "y":
            try:
                move_distance = int(input("How long (1-3 seconds) do you want the robot to move? "))
                if move_distance < 1 or move_distance > 3:
                    print("Invalid distance! Enter a number between 1 and 3.")
                    continue

                print("Select a direction: \n1: Forward\n2: Backward\n3: Left Turn\n4: Right Turn")
                direction = int(input("Enter the number corresponding to the direction: "))

                if direction == 1:
                    print("Moving forward!")
                    safe_move(move_distance)
                elif direction == 2:
                    print("Moving backward!")
                    backward(move_distance)
                elif direction == 3:
                    print("Turning left!")
                    turn_left(move_distance)
                elif direction == 4:
                    print("Turning right!")
                    turn_right(move_distance)
                else:
                    print("Invalid direction! Try again.")
                    continue

                # Read sonar after every move
                read_sonars()

            except ValueError:
                print("Invalid input! Please enter numeric values only.")
                continue

        elif user_input == "auto":
            autonomous_mode()

        elif user_input == "remote":
            remote_control()

        elif user_input == "n":
            robot.exit()
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please enter 'y', 'n', 'auto', or 'remote'.")

# Run the main program
if __name__ == "__main__":
    main()

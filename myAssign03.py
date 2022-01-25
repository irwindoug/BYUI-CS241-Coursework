'''
Program: myAssign03.py
Brother Mellor, CS 241
Author: Doug Irwin
Summary: Creates a robot that moves around a 10x10 field and shoots lasers.
'''

class Robot(object):
    # Initiate 
    def __init__(self, x=10, y=10, fuel=100):
        self.x_coordinate = x
        self.y_coordinate = y
        self.fuel = fuel
    
    def laser(self):
        self.fuel -= 15 # Use fuel to fire laser
        print("Pew! Pew!")

    def move(self, direction):
        if direction == "right": # Use fuel to move robot right
            self.x_coordinate += 1
            self.fuel -= 5
        elif direction == "left": # Use fuel to move robot left
            self.x_coordinate -= 1
            self.fuel -= 5
        elif direction == "up": # Use fuel to move robot up
            self.y_coordinate -= 1
            self.fuel -= 5
        elif direction == "down": # Use fuel to move robot down
            self.y_coordinate += 1
            self.fuel -= 5
        else: # Catch-all for invalid direction
            print("Invalid direction!")

    def check_fuel(self):
        return self.fuel # Return fuel status
 
    def __str__(self):
        return (("(%s, %s) - Fuel: %s") % (self.x_coordinate, self.y_coordinate, self.fuel)) # Return robot status

def game(): # Beginning of game

    robot = Robot() # Create robot
    command = input("Enter command: ") # Initial command

    while command != "quit": # Play game until input equals "quit"
        if (command == "right" or command == "left" or command == "up" or command == "down") and robot.check_fuel() >= 5:
            robot.move(command) # If sufficient fuel to move, move based on user command
        elif command == "fire" and robot.check_fuel() >= 15:
            robot.laser() # If sufficient fuel to fire laser, open fire
        elif (command == "fire" and robot.check_fuel() < 15) or ((command == "right" or command == "left" or command == "up" or command == "down") and robot.check_fuel() < 5):
            print("Insufficient fuel to perform action") # Catch-all if not enough fuel
        elif command == "status":
            print(robot) # Display status of robot
        command = input("Enter command: ")

    print("Goodbye.") # Display when user quits game

def main():
    game() # Start game

if __name__ == "__main__":
    main() # Run main
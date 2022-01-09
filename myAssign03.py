class Robot(object):
    def __init__(self, x=10, y=10, fuel=100):
        self.x_coordinate = x
        self.y_coordinate = y
        self.fuel = fuel
    
    def laser(self):
        self.fuel -= 15
        print("Pew! Pew!")

    def move(self, direction):
        if direction == "right":
            self.x_coordinate += 1
            self.fuel -= 5
        elif direction == "left":
            self.x_coordinate -= 1
            self.fuel -= 5
        elif direction == "up":
            self.y_coordinate -= 1
            self.fuel -= 5
        elif direction == "down":
            self.y_coordinate += 1
            self.fuel -= 5
        else:
            print("Invalid direction!")

    def check_fuel(self):
        return self.fuel
 
    def __str__(self):
        return (("(%s, %s) - Fuel: %s") % (self.x_coordinate, self.y_coordinate, self.fuel))

def game():

    robot = Robot()
    command = input("Enter command: ")

    while command != "quit":
        if (command == "right" or command == "left" or command == "up" or command == "down") and robot.check_fuel() >= 5:
            robot.move(command)
        elif command == "fire" and robot.check_fuel() >= 15:
            robot.laser()
        elif (command == "fire" and robot.check_fuel() < 15) or ((command == "right" or command == "left" or command == "up" or command == "down") and robot.check_fuel() < 5):
            print("Insufficient fuel to perform action")
        elif command == "status":
            print(robot)
        command = input("Enter command: ")

    print("Goodbye.") 

def main():
    game()

if __name__ == "__main__":
    main()
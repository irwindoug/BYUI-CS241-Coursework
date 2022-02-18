"""
File: check07b.py
Author: Br. Burton

Demonstrates abstract base classes.
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, name:str) -> None:
        self.name:str = name

    def display(self) -> None:
        print("{} - {:.2f}".format(self.name, self.get_area()))

    @abstractmethod
    def get_area(self):
        return NotImplementedError()

class Circle(Shape):

    def __init__(self, radius=0.0) -> None:
        super().__init__("Circle")
        self.radius:float = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length=0.0, width=0.0) -> None:
        super().__init__("Rectangle")
        self.length:float = length
        self.width:float = width


    def get_area(self):
        return self.length * self.width


def main():

    shapes = []
    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            shapes.append(Circle(radius))
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            shapes.append(Rectangle(length,width))


    # Done entering shapes, now lets print them all out:
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()


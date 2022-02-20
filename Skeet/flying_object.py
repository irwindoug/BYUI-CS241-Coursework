# Library imports
from abc import ABC, abstractmethod

# Base class imports
from velocity import Velocity
from point import Point

class FlyingObject(ABC):
    def __init__(self, radius:float, color:str, speed:float=1) -> None:
        self.center:Point = Point() # Default center point is (0,0)
        self.velocity:Velocity = Velocity(speed, speed) # Speed is optional param, otherwise defaults as 1
        self.radius:float = radius # Required param
        self.color:str = color # Required param
        self.alive:bool = True # Set to alive when created

    # Draw function MUST be defined by child class; otherwise, error will be thrown
    @abstractmethod
    def draw(self) -> None:
        return NotImplementedError()

    # Default advance function moves based off of defined velocity
    def advance(self) -> None:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    # Return whether or not the object is off the screen
    def is_off_screen(self, screen_width, screen_height) -> bool:
        return (self.center.y >= screen_height or self.center.x >= screen_width or self.center.x < 0 or self.center.y < 0)
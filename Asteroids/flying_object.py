# Library imports
import arcade
from abc import ABC

# Base class imports
from velocity import Velocity
from point import Point

class FlyingObject(ABC):
    def __init__(self, img:str, radius:float, speed:float=0, angle:float=0) -> None:
        self.center:Point = Point() # Default center point is (0,0)
        self.velocity:Velocity = Velocity(speed, speed) # Speed is optional param, otherwise defaults as 1
        self.texture = arcade.load_texture(img) # Required param
        self.direction:float = 1
        self.speed:float = speed
        self.radius:float = radius # Required param
        self.angle:float = angle
        self.alive:bool = True # Set to alive when created

    def draw(self) -> None:
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle)

    # Default advance function moves based off of defined velocity
    def advance(self, screen_width, screen_height) -> None:
        self.wrap(screen_width, screen_height)
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @property
    def is_alive(self) -> bool:
        return self.alive

    def wrap(self, screen_width, screen_height):
        if self.center.x > screen_width: self.center.x -= screen_width
        if self.center.x < 0: self.center.x += screen_width
        if self.center.y > screen_height: self.center.y -= screen_height
        if self.center.y < 0: self.center.y += screen_height
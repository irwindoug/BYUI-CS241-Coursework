# Library imports
import arcade
from abc import ABC

# Base class imports
from velocity import Velocity
from point import Point

class FlyingObject(ABC):
    """
    Baseclass

    """
    def __init__(self, img:str, radius:float, speed:float=0, angle:float=0) -> None:
        self.center:Point = Point()
        self.velocity:Velocity = Velocity()
        self.texture = arcade.load_texture(img)
        self.alive:bool = True
        self.radius:float = radius # Required param
        self.turn = angle
        self.angle:float = 0
        self.speed:float = speed

    def draw(self) -> None:
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.texture.width, self.texture.height, self.texture, self.angle)

    # Default advance function moves based off of defined velocity
    def advance(self, screen_width, screen_height) -> None:
        self.wrap(screen_width, screen_height)
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @property
    def is_alive(self) -> bool:
        """
        Returns if the object is alive or not
        """
        return self.alive

    def wrap(self, screen_width, screen_height):
        if self.center.x > screen_width: self.center.x -= screen_width
        if self.center.x < 0: self.center.x += screen_width
        if self.center.y > screen_height: self.center.y -= screen_height
        if self.center.y < 0: self.center.y += screen_height
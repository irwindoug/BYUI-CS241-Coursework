# Library imports
import arcade
import math

# Base class imports
from flying_object import FlyingObject

# Root bullet defaults
BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

class Bullet(FlyingObject):
    def __init__(self) -> None:
        # Initialize object defaults
        super().__init__(BULLET_RADIUS, BULLET_COLOR, BULLET_SPEED) 

    def draw(self) -> None:
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    #  Fire bullet based on rifle angle
    def fire(self, angle:float) -> None:
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
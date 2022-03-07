# Library imports
import math

# Base class imports
from flying_object import FlyingObject

# Root bullet defaults
BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_IMAGE = "images/laserBlue01.png"

class Bullet(FlyingObject):
    def __init__(self) -> None:
        # Initialize object defaults
        super().__init__(BULLET_IMAGE, BULLET_RADIUS, BULLET_SPEED) 

    #  Fire bullet based on rifle angle
    def fire(self, angle:float) -> None:
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
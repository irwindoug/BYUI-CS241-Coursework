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
    def __init__(self, angle, ship_position, ship_speed) -> None:
        # Initialize object defaults
        super().__init__(BULLET_IMAGE, BULLET_RADIUS, BULLET_SPEED)
        self.center.x = ship_position.x
        self.center.y = ship_position.y
        self.velocity.dx += ship_speed.dx
        self.velocity.dy += ship_speed.dy
        self.angle = angle+90
        self.life = BULLET_LIFE

    @property
    def fire(self) -> None:
        """
         Creates a bullet object
        """
        self.velocity.dx -= math.sin(math.radians(self.angle-90)) * self.speed
        self.velocity.dy += math.cos(math.radians(self.angle-90)) * self.speed

    def advance(self, screen_width, screen_height) -> None:
        super().advance(screen_width, screen_height)
        self.life -= 1
        if self.life <= 0: self.alive = False
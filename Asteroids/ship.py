import math
from explosion import Particle

PARTICLE_COUNT = 20

# Global Variables
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30
SHIP_IMAGE = "images/playerShip1_orange.png"

# Local Imports
from flying_object import FlyingObject

class Ship(FlyingObject):
    def __init__(self, screen_width, screen_height) -> None:
        super().__init__(SHIP_IMAGE, SHIP_RADIUS, SHIP_THRUST_AMOUNT, SHIP_TURN_AMOUNT)
        self.center.x = screen_width/2
        self.center.y = screen_height/2

    @property
    def left(self) -> None:
        self.angle += self.turn

    @property
    def right(self) -> None:
        self.angle -= self.turn

    def thrust(self, isUp) -> None:
        if (not isUp):
            self.velocity.dx += math.sin(math.radians(self.angle)) * self.speed
            self.velocity.dy -= math.cos(math.radians(self.angle)) * self.speed
        else:
            self.velocity.dx -= math.sin(math.radians(self.angle)) * self.speed
            self.velocity.dy += math.cos(math.radians(self.angle)) * self.speed


    def hit(self, explosion_list) -> None:
        self.alive = False 
        self.alpha = 0
        self.velocity.dx = 0
        self.velocity.dy = 0
        for i in range(PARTICLE_COUNT):
            particle = Particle(explosion_list)
            particle.center_x = self.center.x
            particle.center_y = self.center.y
            explosion_list.append(particle)
        return explosion_list
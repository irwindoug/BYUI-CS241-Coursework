import random
import math
from flying_object import FlyingObject

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15
BIG_ROCK_IMAGE = "images/meteorGrey_big1.png"

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_IMAGE = "images/meteorGrey_med1.png"

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_IMAGE = "images/meteorGrey_small1.png"

class Rock(FlyingObject):
    def __init__(self, img: str, radius: float, speed: float = 1, angle:float = 0) -> None:
        super().__init__(img, radius, speed, angle)
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed


class LargeRock(Rock):
    def __init__(self) -> None:
        super().__init__(BIG_ROCK_IMAGE, BIG_ROCK_RADIUS, BIG_ROCK_SPEED, BIG_ROCK_SPIN)


class MediumRock(Rock):
    def __init__(self) -> None:
        super().__init__(MEDIUM_ROCK_IMAGE, MEDIUM_ROCK_RADIUS)

class SmallRock(Rock):
    def __init__(self) -> None:
        super().__init__(SMALL_ROCK_IMAGE, SMALL_ROCK_RADIUS)

import random
import math
from abc import ABC, abstractmethod
from flying_object import FlyingObject
from velocity import Velocity

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

class Rock(FlyingObject, ABC):
    def __init__(self, img: str, radius: float, angle:float = 0, speed: float = 1) -> None:
        super().__init__(img, radius, speed, angle)
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    def advance(self, screen_width, screen_height):
        super().advance(screen_width, screen_height)
        self.angle += self.turn

    @abstractmethod
    def hit(self) -> None:
        return NotImplementedError()

class LargeRock(Rock):
    def __init__(self) -> None:
        super().__init__(BIG_ROCK_IMAGE, BIG_ROCK_RADIUS, BIG_ROCK_SPIN, BIG_ROCK_SPEED)

    @property
    def hit(self) -> None:
        asteroids = [MediumRock(), MediumRock(),SmallRock()]

        for asteroid in asteroids:
            asteroid.center.x = self.center.x
            asteroid.center.y = self.center.y

        asteroids[0].velocity.dy = self.velocity.dy + 2
        asteroids[1].velocity.dy = self.velocity.dy - 2
        asteroids[2].velocity.dx = self.velocity.dx + 5

        self.alive = False
        return asteroids


class MediumRock(Rock):
    def __init__(self) -> None:
        super().__init__(MEDIUM_ROCK_IMAGE, MEDIUM_ROCK_RADIUS, MEDIUM_ROCK_SPIN)

    @property
    def hit(self) -> None:
        asteroids = [SmallRock(), SmallRock()]

        for asteroid in asteroids:
            asteroid.center.x = self.center.x
            asteroid.center.y = self.center.y

        asteroids[0].velocity = Velocity(self.velocity.dx + 1.5, self.velocity.dy + 1.5)
        asteroids[1].velocity = Velocity(self.velocity.dx - 1.5, self.velocity.dy - 1.5)

        self.alive = False
        return asteroids

class SmallRock(Rock):
    def __init__(self) -> None:
        super().__init__(SMALL_ROCK_IMAGE, SMALL_ROCK_RADIUS, SMALL_ROCK_SPIN)

    @property
    def hit(self) -> None:
        self.alive = False
        return []

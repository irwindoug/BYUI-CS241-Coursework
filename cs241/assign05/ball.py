import arcade
import random
import math
from point import Point
from velocity import Velocity

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
BALL_RADIUS = 10
MOVE_AMOUNT = 2

class Ball:
    def __init__(self):
        self.center = Point(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.velocity = Velocity(MOVE_AMOUNT,MOVE_AMOUNT)

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.RED)

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def bounce_horizontal(self):
        self.velocity.dx *= -1

    def bounce_vertical(self):
        self.velocity.dy *= -1

    def restart(self):
        self.center = Point(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.velocity.dx = MOVE_AMOUNT * math.sin(random.uniform(0, 360))
        self.velocity.dy = MOVE_AMOUNT * math.sin(random.uniform(0, 360))
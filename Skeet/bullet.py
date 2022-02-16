import arcade
import math

from flying_object import FlyingObject

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

class Bullet(FlyingObject):
    def __init__(self) -> None:
        super().__init__(BULLET_RADIUS, BULLET_COLOR)
        self.radius = BULLET_RADIUS
        self.velocity.dx = BULLET_SPEED
        self.velocity.dy = BULLET_SPEED

    def advance(self) -> None:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self) -> None:
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def is_off_screen(self, screen_width, screen_height) -> bool:
        return (self.center.x >= screen_height or self.center.y >= screen_width or self.center.x < 0 or self.center.y < 0)

    def fire(self, angle:float) -> None:
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
import arcade
import random

from flying_object import FlyingObject

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_RADIUS = 15
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE

class Target(FlyingObject):
    def __init__(self, target_type:str, screen_height) -> None:
        self.target_type = target_type
        
        if self.target_type == "strong":
            self.lives = 3
        else:
            self.lives = 1
        
        if self.target_type == "standard" or self.target_type == "strong":
            radius = TARGET_RADIUS
            color = TARGET_COLOR
        elif self.target_type == "safe":
            radius = TARGET_SAFE_RADIUS
            color = TARGET_SAFE_COLOR
        super().__init__(radius, color)


        self.center.y = random.randint(screen_height/2, screen_height)

    def advance(self) -> None:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    def draw(self) -> None:
        if self.target_type == "strong":
            arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
            text_x = self.center.x - (self.radius / 2)
            text_y = self.center.y - (self.radius / 2)
            arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)
        else:
            arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    def is_off_screen(self, screen_width, screen_height) -> bool:
        return (self.center.x >= screen_height or self.center.y >= screen_width or self.center.x < 0 or self.center.y < 0)

    def hit(self) -> int:
        self.lives -= 1
        if self.lives == 0:
            self.alive = False
        return 1
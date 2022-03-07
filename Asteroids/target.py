# Library imports
import arcade
import random

# Base class imports
from flying_object import FlyingObject

# Root target defaults
TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_RADIUS = 15
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE

class Target(FlyingObject):
    def __init__(self, target_type:str, screen_height) -> None:
        self.target_type = target_type # Define what type of target
        
        # If the target type is strong, live count is 3; otherwise, it is 1
        if self.target_type == "strong":
            self.lives = 3
        else:
            self.lives = 1
        
        # Determine color based off of tartget type
        if self.target_type == "safe":
            radius = TARGET_SAFE_RADIUS
            color = TARGET_SAFE_COLOR
        else:
            radius = TARGET_RADIUS
            color = TARGET_COLOR

        # Initialize default variables from FlyingObject with target type defaults
        super().__init__(radius, color)

        # Initialize target center somewhere between the middle and top of the screen
        self.center.y = random.randint(screen_height/2, screen_height)

    def draw(self) -> None:

        # Draw circle outline with number for strong target type
        if self.target_type == "strong":
            arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
            text_x = self.center.x - (self.radius / 2)
            text_y = self.center.y - (self.radius / 2)
            arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)
        
        #  Draw filled square for safe target type
        elif self.target_type == "safe":
            arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius*2, self.radius*2, self.color)

        # Draw default circle
        else:
            arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)
  

    def hit(self) -> int:

        # Deduct life and check if target is still alive
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

        

        """
        Points awarded is based on the following conditions:
        Strong Targets (First two hits): 1 point
        Strong Targets (Final hit): 5 points
        Standard Targets: 1 point
        Safe Targets: -10 points

        Safe targets should NOT be hit and will result in a penalty deduction
        """
        if (self.target_type == "strong" and self.lives == 0):
            points = 5
        elif self.target_type == "safe":
            points = -10
        else:
            points = 1
        return points
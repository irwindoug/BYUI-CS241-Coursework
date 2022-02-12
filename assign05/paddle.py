'''
Assignment: Week 5 - Paddle Class
Brother Mellor, CS 241
Author: Doug Irwin
'''

import arcade
from point import Point

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

class Paddle:
    def __init__(self):
        self.center = Point(SCREEN_WIDTH, SCREEN_HEIGHT/2)

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x,self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.SMOKY_BLACK)

    def move_up(self):
        if self.center.y <= SCREEN_HEIGHT - (PADDLE_HEIGHT/2):
            self.center.y += MOVE_AMOUNT

    def move_down(self):
        if self.center.y >= 0 + (PADDLE_HEIGHT/2):
            self.center.y -= MOVE_AMOUNT
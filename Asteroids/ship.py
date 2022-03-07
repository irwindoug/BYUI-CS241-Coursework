# Global Variables
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30
SHIP_IMAGE = "images/playerShip1_orange.png"

# Local Imports
from flying_object import FlyingObject

class Ship(FlyingObject):
    def __init__(self, screen_width, screen_height) -> None:
        super().__init__(SHIP_IMAGE, SHIP_RADIUS)
        self.center.x = screen_width/2
        self.center.y = screen_height/2


    def left(self) -> None:
        pass

    def right(self) -> None:
        pass

    def thrust(self) -> None:
        pass
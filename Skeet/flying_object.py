from velocity import Velocity
from point import Point

class FlyingObject():
    def __init__(self, radius:float, color:str) -> None:
        self.center:Point = Point()
        self.velocity:Velocity = Velocity()
        self.radius:float = radius
        self.color:str = color
        self.alive:bool = True
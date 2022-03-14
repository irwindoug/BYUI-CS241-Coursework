"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
# Global Imports
import arcade
from bullet import Bullet

# Local Imports
from ship import Ship
from rock import LargeRock

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ROCK_COUNT = 5


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # declare anything here you need the game class to track
        self.ship = Ship(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.asteroids = []
        self.bullets = []

        for i in range(INITIAL_ROCK_COUNT):
            self.asteroids.append(LargeRock())


    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        for bullet in self.bullets:
            bullet.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

        self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance(SCREEN_WIDTH, SCREEN_WIDTH)

        for bullet in self.bullets:
            bullet.advance(SCREEN_WIDTH, SCREEN_WIDTH)

        self.ship.advance(SCREEN_WIDTH, SCREEN_WIDTH)

        # Check for collisions
        self.check_collisions()

    def check_collisions(self):

        def collided(object1: object, object2: object) -> bool:
            """ This function checks to see if both object radius's are overlapping, and returns a True or False value.\n
                Arguments:
                    object1 {object} - First object to compare\n
                    object2 {object} - Second object to compare

                Logic: Check if the distance between both x and y coordinates are less than both objects' radius
            """
            return (object1.is_alive and object2.is_alive) and ((abs(object1.center.x - object2.center.x) < (object1.radius + object2.radius)) and (abs(object1.center.y - object2.center.y) < (object1.radius + object2.radius)))

        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if collided(bullet, asteroid):
                    bullet.alive = False
                    self.asteroids.extend(asteroid.hit)

        for asteroid in self.asteroids:
            if collided(asteroid, self.ship):
                self.ship.alive = False
                self.ship.velocity.dx = 0
                self.ship.velocity.dy = 0
                self.asteroids.extend(asteroid.hit)

        

        self.remove_dead()

    def remove_dead(self) -> None:
        """
        Removes any object that isn't alive
        """
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.is_alive:
                self.asteroids.remove(asteroid)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right

        if arcade.key.UP in self.held_keys:
            self.ship.thrust(True)

        if arcade.key.DOWN in self.held_keys:
            self.ship.thrust(False)

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
        #    bullet = Bullet(self.ship.angle, self.ship.center)
        #    self.bullets.append(bullet)
        #    bullet.fire

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.is_alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # Fire the bullet here!
                bullet = Bullet(self.ship.angle, self.ship.center, self.ship.velocity)
                self.bullets.append(bullet)
                bullet.fire

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()

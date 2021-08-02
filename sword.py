# Import everything in ursina
from ursina import *

# Make the Sword class
class Sword(FrameAnimation3d):
    def __init__(self, position = (1.5, -2.2, 1.8), rotation = (0, 90, 0)):
        super().__init__(
            # Get every model that starts with 'sword_'
            "sword_",
            # Makes it go at a 100 frames per second
            fps = 100,
            frame_times = 140,
            # Stops it from playing it immediately
            autoplay = False,
            # Makes it loop
            loop = True,
            position = position,
            rotation = rotation,
            scale = (4, 4, 4),
            # Add a texture to the sword
            texture = "sword",
            # Parent it to the camera so its stuck
            parent = camera
        )

        # Pauses it
        self.pause()

    # Built in ursina function
    def input(self, key):
        # If left mouse is pressed, resume the animation
        if key == "left mouse down":
            self.resume()
            invoke(self.pause, delay = 1.4)

# Import all of ursina
from ursina import *

# Import the player class
from player import Player

# Import the sword
from sword import *

# Declare the app
app = Ursina()

# Make the player
player = Player("cube", (0, 10, 0), "box")
player.SPEED = 2
player.jump_height = 0.3

# Make the ground
ground = Entity(model = "cube", scale = (100, 1, 100), collider = "box", color = color.light_gray, texture = "white_cube")

# Lighting
PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

# Add skybox
Sky()

# Declare sword
sword = Sword()

# Run the app
app.run()

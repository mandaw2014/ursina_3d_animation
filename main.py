from ursina import *
from player import Player
from sword import *

app = Ursina()

player = Player("cube", (0, 10, 0), "box")
player.SPEED = 2
player.jump_height = 0.3

ground = Entity(model = "cube", scale = (100, 1, 100), collider = "box", color = color.light_gray, texture = "white_cube")

PointLight(parent = camera, color = color.white, position = (0, 10, -1.5))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

Sky()

sword = Sword()

app.run()
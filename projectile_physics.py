import math
from vector2d import Vector2D

class Environment:
    def __init__(self):
        self.gravity = 9.81
        self.airdensity = 1.225

class Projectile:
    def __init__(self, launchspeed, angle, mass):
        self.history = []
        self.velocity = Vector2D(
            launchspeed * math.cos(math.radians(angle)),
            launchspeed * math.sin(math.radians(angle))
        )
        self.position = Vector2D(0,0)
        self.mass = mass


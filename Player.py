import pygame, sys, math, components


class Player:
    def __init__(self, x=100, y=100):
        self.position = components.Position(x, y)
        self.velocity = components.Velocity(0, 0)
        self.acceleration = components.Acceleration(0, 0)
        self.orientation = components.Orientation(0)
        self.color = components.Color(21, 11, 134)
        self.size = components.Size(18, 40)


import pygame


class Player:
    pass


class Position(pygame.Vector2):
    pass


class Velocity(pygame.Vector2):
    pass


class Acceleration(pygame.Vector2):
    pass


class Orientation:
    def __init__(self, deg):
        self.deg = deg


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class IntegerPoint:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Color:
    def __init__(self, r, g, b, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def rgba(self):
        return self.r, self.g, self.b, self.a

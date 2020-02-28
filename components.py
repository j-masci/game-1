import pygame, funcs, math


class Vector2(pygame.Vector2):

    def move_in_direction(self, radius, deg):
        theta = funcs.to_rad(deg)
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        self.x = self.x + x
        self.y = self.y + y


class PlayerTag:
    pass


class Position(Vector2):
    pass


class Velocity(Vector2):
    pass


class Acceleration(Vector2):
    pass


# a vector of points
class Shape:
    def __init__(self):
        self.points = []


# a vector of points
class Shape1D(Shape):
    pass


# a vector of points
class Shape2D(Shape):
    pass







class Orientation:
    def __init__(self, deg):
        self.deg = deg

    def radians(self):
        return funcs.to_rad(self.deg)


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


# a player should...
# have a position component
# have an orientation component
# have a polygon component (a vector of points)
# ok great so fucking simple
# but what about when we have no choice but to store
# both the center point and the outer points.
# how do we declare data dependencies among components so that
# data doesn't become stale?
# the simplest method is to store methods in entities that act on
# multiple components, but, then re-usability points towards inheritance
# which I want to avoid mostly.
# maybe @property or __set_attr but idk.
# its more about a declarative way to say that property X of component Y
# upon changing, needs to invalidate property A of component B, or something
# like that. but, this is only a dependency among two properties, there may
# be cases with 3 or more components. also, this corresponds to properties
# of components, why not just values in the first place ?
# furthermore, data constraints are not component based, they are context based,
# a component might be used in multiple entities where the constraint only
# exists in some of them.
# perhaps, values that need to trigger callbacks on change can use a class
# but I need to look into how this affects objects, vectors, etc.
# also does python have the necessary magic methods to make the single
# variable behave like a normal variable so that we don't need to know
# whether or not its an object wrapping a variable or just a plain old variable.
# perhaps, we can just extend the Int or String classes or w/e.
# that being said, does the component need to care whether it stores built-in
# value types or a special type that reacts to mutation.
# furthermore, this is still an issue because what if a component itself should
# react to mutation, rather than registering a callback to all properties of
# a component on change.


class MutableScalar:
    def __init__(self):
        pass

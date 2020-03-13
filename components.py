import game


# forces/momentum/etc
# velocity: do we store it on the player?
# is it calculated before or after moving?
# every time we move to we store it .... ?
# this causes issues if we move more than once
# in the same update loop.
# ie, having multiple forces act on the object
# do we set velocity and have the player move according to the velocity?
# i don't fucking know. if we do that, then how to we change the position
# on its own ???
# momentum can be thought of as a force, its the product of velocity with weight
# momentum is counter acted by friction perhaps
# friction is interesting if we try to calculate it based on the entire surface
# of an object. also what if the object is rotating, or what if the object has
# non constant friction co-efficients...
# perhaps we don't store position ever
# we only store multiple forces acting in different ways upon the same
# object. each frame, all of those forces are used to determine the next position.
# but still what about momentum, is it derived by differences in positions multiplied
# by mass.... or we do we just store it as a force that also needs to be updated ?? fuck that
# makes no sense.


class Vector2(game.pygame.Vector2):

    def move_in_direction(self, magnitude, deg):
        theta = game.utils.to_rad(deg)
        x = magnitude * game.math.cos(theta)
        y = magnitude * game.math.sin(theta)

        self.x = self.x + x
        self.y = self.y + y

    def to_tuple(self):
        return self.x, self.y

    # generally good for positions, not for velocity
    def to_tuple_using_ints(self):
        return int(self.x), int(self.y)

    def copy(self):
        return Position(self.x, self.y)


class RotationalForce:
    def __init__(self, units):
        self.units = units

    # maps self.units to the range (-1 + error, 1 - error)
    # this isnt working well right now its complicated..
    # i mean this function works fine but the idea does not because
    # self.units just keeps growing and then we cant easily turn the other
    # direction unless we can invert the sigmoid function which sucks balls
    def sigmoid(self, error=0.01):
        return game.mapping_functions.sigmoid_rounded(self.units, error)


class Velocity(Vector2):
    pass


class Acceleration(Vector2):
    pass


class Weight:
    def __init__(self, units):
        self.units = units


class PlayerTag:
    pass


class PersonTag:
    pass


class Position(Vector2):
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


class UIComponent:
    __slots__ = ['draw', 'on_click']

    def __init__(self):
        pass


class Orientation:

    def __init__(self, _degrees):
        self.degrees = _degrees

    @property
    def degrees(self):
        return self._degrees

    @degrees.setter
    def degrees(self, value):
        self._degrees = game.utils.fix_degrees(value)

    @property
    def radians(self):
        return game.utils.to_rad(self.degrees)

    @radians.setter
    def radians(self, value):
        self._degrees = game.utils.fix_degrees(game.utils.to_deg(value))

    def unit_vector(self):
        v = Vector2()
        v.from_polar((1, self.degrees - 90))
        return v

    # approach target degrees by shortest "radial" path, without going
    # beyond the target.
    @staticmethod
    def approach_value(current_degrees, target_degrees, step):

        fix = game.utils.fix_degrees

        c = fix(current_degrees)
        t = fix(target_degrees)

        get_dir = Orientation.get_optimal_direction
        direction = get_dir(c, t)

        # if optimal direction changes, we over stepped
        if direction is -1:
            dest = fix(c - step)
            return dest if get_dir(dest, t) is -1 else t
        elif direction is 1:
            dest = fix(c + step)
            return dest if get_dir(dest, t) is 1 else t
        else:
            game.player.color.set(100, 100, 100)
            return c

    @staticmethod
    def get_optimal_direction(current_degrees, target_degrees):
        """
        >>> Orientation.get_optimal_direction(181, 0)
        1
        >>> Orientation.get_optimal_direction(355, 5)
        1
        >>> Orientation.get_optimal_direction(5, 355)
        -1
        >>> Orientation.get_optimal_direction(179, 0)
        -1
        >>> Orientation.get_optimal_direction(0, 360)
        0
        >>> Orientation.get_optimal_direction(180, 0)
        0
        >>> Orientation.get_optimal_direction(0, 180)
        0
        >>> Orientation.get_optimal_direction(0, 179)
        1
        >>> Orientation.get_optimal_direction(0, 181)
        -1
        """
        c = game.utils.fix_degrees(current_degrees)
        t = game.utils.fix_degrees(target_degrees)

        diff = game.utils.fix_degrees(c - t)

        if diff is 0:
            return 0
        elif diff is 180:
            return 0
        elif diff > 180:
            return 1
        else:
            return -1


class IntegerPoint:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Color:
    def __init__(self, r, g, b, a=1):
        self.r = False
        self.g = False
        self.b = False
        self.a = False
        self.set(r, g, b, a)

    @staticmethod
    def random_instance():
        r = game.random.randint
        return Color(r(0, 255), r(0, 255), r(0, 255))

    def set(self, r, g, b, a=1):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def rgba(self):
        return self.r, self.g, self.b, self.a

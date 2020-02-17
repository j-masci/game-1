import pygame, math
# functions that can be called on entities
# i don't know if this is the ideal place to put those functions
# eventually this file will get large.
# the idea is to try to avoid too much inheritance.
# we do this by focusing classes on data and not on
# methods. a human should not have a get_rect() method
# in my opinion. instead, get_rect() should be a function
# that works on any object containing a position and an orientation
# but then, should we not just make the function accept the position
# and orientating? I don't fucking know. we'll inevitably
# have to make this decision about a billion times. passing in
# an object is much easier and will simply fail if the object
# does not have the necessary data. passing in primitive
# values (or components) is much more concise but is also
# a pain in the ass. furthermore, objects will be pass by
# ref, and how will this affect caching of computation?
# if we pass in primitive values its even more of a pain
# in the ass, but we'll be able to memoize or use lru_cache
# perhaps we can use multiple functions but this is clearly
# a massive fucking p.i.t.a. now for every functions do we
# just fucking write 3 instead? one accepting an object,
# one accepting components of that object, and one
# accepting primitive values that has a caching layer?
# pretty lame. maybe we just bite the bullet and use
# primitives always. i have no clue. will be faster,
# but will it matter?


# this will be so fun after we have about 100 classes like this
class GetRect:

    @staticmethod
    def via_object(obj):
        return GetRect.via_components(obj.position, obj.size, obj.orientation)
        pass

    @staticmethod
    def via_components(position, size, orientation):
        return GetRect.via_primitives(position.x, position.y, size.width, size.height, orientation.deg)
        pass

    # for now, returns 4 points, which can be used to construct a polygon
    # when we do collision, we might have to find out how to use the rect object
    # and rotate it
    @staticmethod
    def via_primitives(x, y, width, height, deg):
        center = (x, y)
        w2 = width/2
        h2 = height/2
        points = []
        points.append(RotatePoint(center, (x - w2, y - h2), deg))
        points.append(RotatePoint(center, (x - w2, y + h2), deg))
        points.append(RotatePoint(center, (x + w2, y + h2), deg))
        points.append(RotatePoint(center, (x + w2, y - h2), deg))
        return points




# https://stackoverflow.com/questions/32572267/how-to-rotate-a-triangle-pygame
def RotatePoint(c, p, r):
    x = c[0]*math.cos(r)-c[0]+c[1]*math.sin(r)+p[0]*math.cos(r)+p[1]*math.sin(r)
    y = -c[0]*math.sin(r)+c[1]*math.cos(r)-c[1]-p[0]*math.sin(r)+p[1]*math.cos(r)
    return (x, y)
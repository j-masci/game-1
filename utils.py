import game, math
import components as c


def debug_append(event, data=None):
    a = [event, game.timer.time_since_start()]

    if data is not None:
        a.append(data)

    game.debugger.data.append(a)


class GetRect:

    @staticmethod
    def via_object(obj):
        return GetRect.via_components(obj.position, obj.size, obj.orientation)

    @staticmethod
    def via_components(position, size, orientation):
        return GetRect.via_primitives(position.x, position.y, size.width, size.height, orientation.degrees)

    # for now, returns 4 points, which can be used to construct a polygon
    # when we do collision, we might have to find out how to use the rect object
    # and rotate it
    @staticmethod
    def via_primitives(x, y, width, height, deg):
        center = (x, y)
        w2 = width / 2
        h2 = height / 2
        return [
            rotate_point(center, (x - w2, y - h2), deg),
            rotate_point(center, (x - w2, y + h2), deg),
            rotate_point(center, (x + w2, y + h2), deg),
            rotate_point(center, (x + w2, y - h2), deg)
        ]


# rotate a point around another point
def rotate_point(origin, point, deg):
    rad = to_rad(deg)

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(rad) * (px - ox) - math.sin(rad) * (py - oy)
    qy = oy + math.sin(rad) * (px - ox) + math.cos(rad) * (py - oy)
    return qx, qy


def to_rad(deg):
    return math.pi * deg / 180


def to_deg(rad):
    return rad * (180 / math.pi)


def fix_degrees(deg):
    # unsure how this might affect ints/floats
    deg = deg % 360
    return deg

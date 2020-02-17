import pygame, sys, math, components


class Player:

    # todo: we might have to store a rect as data and update it upon changing
    # position or orientation. for now, rect is derived, but, if we had say
    # 100 entities on screen doing collision detection, we might have to store
    # the data twice.
    def __init__(self, x=100, y=100):
        self.position = components.Position(x, y)
        self.velocity = components.Velocity(0, 0)
        self.acceleration = components.Acceleration(0, 0)
        self.orientation = components.Orientation(0)
        self.color = components.Color(21, 11, 134)
        self.size = components.Size(10, 30)

    def mouse_ev_1(self, x, y, app):

        dist = pygame.Vector2(x, y).distance_to(app.center)
        spd = dist * 0.05 ** 0.4
        spd = min(spd, 20)

        print(spd)

        self.velocity.x = x - app.center.x
        self.velocity.y = y - app.center.y

        if self.velocity.magnitude() > 0:
            self.velocity.scale_to_length(spd)
        else:
            self.velocity.x = self.velocity.y = 0
import pygame, sys, math


class Player:

    def __init__(self, x, y, size=20, color=(55, 12, 111)):

        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.size = int(size)
        self.color = pygame.Color(*color)

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

    def event(self, ev, app):

        if ev.type == pygame.MOUSEMOTION:
            self.mouse_ev_1(ev.pos[0], ev.pos[1], app)

        pass

    def update(self, app):

        self.velocity.x = self.velocity.x + self.acceleration.x
        self.velocity.y = self.velocity.y + self.acceleration.y

        self.pos.x = self.pos.x + self.velocity.x
        self.pos.y = self.pos.y + self.velocity.y

        self.pos.x = max(0, self.pos.x)
        self.pos.x = min(self.pos.x, app.size.x)

        self.pos.y = max(0, self.pos.y)
        self.pos.y = min(self.pos.y, app.size.y)

    def draw(self, display):

        # pygame.draw.line(display, pygame.color(255, 255, 255))
        pygame.draw.circle(display, self.color, (int(self.pos.x), int(self.pos.y)), int(self.size))

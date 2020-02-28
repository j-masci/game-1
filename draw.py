import pygame, math, sys, collections
import components, processors, funcs


def draw(app):
    _player(app)
    _lines(app)


def _lines(app):
    pygame.draw.line(app.display, (0, 0, 0), (0, app.center.y), (app.size.x, app.center.y))
    pygame.draw.line(app.display, (0, 0, 0), (app.center.x, 0), (app.center.x, app.size.x))


def _player(app):

    # app.world.get_components(...)

    # player = self.app.player
    # points = funcs.GetRect.via_object(player)
    # pygame.draw.polygon(self.app.display, player.color.rgba(), points)
    pass

import game


def draw():
    _player()
    _lines()


def _lines():

    x0 = game.window.get_center().x
    y0 = game.window.get_center().y

    game.pygame.draw.line(game.display, (0, 0, 0), (0, y0), (game.window.width, y0))
    game.pygame.draw.line(game.display, (0, 0, 0), (x0, 0), (x0, game.window.width))


def _player():
    # app.world.get_components(...)

    # player = self.app.player
    # points = funcs.GetRect.via_object(player)
    # pygame.draw.polygon(self.app.display, player.color.rgba(), points)
    pass

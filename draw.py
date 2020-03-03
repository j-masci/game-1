import game
import components as c


def draw():
    _player()
    _lines()


def _lines():

    x0 = game.window.get_center().x
    y0 = game.window.get_center().y

    game.pygame.draw.line(game.display, (0, 0, 0), (0, y0), (game.window.width, y0))
    game.pygame.draw.line(game.display, (0, 0, 0), (x0, 0), (x0, game.window.width))


def _player():
    player = game.player
    points = game.utils.GetRect.via_object(player)
    game.pygame.draw.polygon(game.display, player.color.rgba(), points)
    pass

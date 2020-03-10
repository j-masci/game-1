import game
import components as c


def draw():

    _draw_lines()

    game.player.draw()

    for e in game.circle_things:
        e.draw()


def _draw_lines():

    x0 = game.window_props.get_center().x
    y0 = game.window_props.get_center().y

    game.pygame.draw.line(game.window_surface, (0, 0, 0), (0, y0), (game.window_props.width, y0))
    game.pygame.draw.line(game.window_surface, (0, 0, 0), (x0, 0), (x0, game.window_props.width))



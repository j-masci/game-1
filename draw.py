import game
import components as c


def draw():
    _draw_lines()
    _draw_persons()
    game.player.draw()


def _draw_lines():
    x0 = game.window_props.get_center().x
    y0 = game.window_props.get_center().y

    game.pygame.draw.line(game.window_surface, (0, 0, 0), (0, y0), (game.window_props.width, y0))
    game.pygame.draw.line(game.window_surface, (0, 0, 0), (x0, 0), (x0, game.window_props.width))


def _draw_persons():
    c = game.components

    for ent, (tag, position, size, color) in game.world.get_components(c.PersonTag, c.Position, c.Size, c.Color):
        game.pygame.draw.circle(game.window_surface, color.rgba(), position.to_tuple(), size.width)



import game
import pprint

state = {}


def draw(surface):

    global state

    state["mouse_pos"] = game.pygame.mouse.get_pos()
    state["mouse_rel"] = game.pygame.mouse.get_rel()
    state["mouse_pressed"] = game.pygame.mouse.get_pressed()
    state["mouse_focused"] = game.pygame.mouse.get_focused()
    state["objects"] = len(game.objects)
    state["can_shoot_at"] = game.player.can_shoot_at

    # very ugly temporary fix to text wrapping problem
    textTop = 0
    for key, val in game.on_screen_debugger.state.items():
        font = game.pygame.font.SysFont("Comic Sans MS", 20)
        textsurface = font.render(pprint.pformat({
            key: val
        }), False, (0, 0, 0))
        surface.blit(textsurface, (0, textTop))
        textTop += 25


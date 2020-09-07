import game
import random
import components as c

Processor = game.esper.Processor


# quit and stuff
class Events(Processor):

    def process(self):

        pg = game.pygame
        keys = game.events.keys_pressed

        # alt-f4.
        # todo: this actually causes a fatal error which happens to be ok for now since that also quits the game.
        if keys[pg.K_F4] and keys[pg.KMOD_ALT]:
            game.init.quit()

        if game.events.key_up_occurred('f5'):
            print("Attempting to restart (todo: not working)")
            game.init.quit(True)

        for ev in game.loop.events:

            # quit
            if ev.type == pg.QUIT:
                game.init.quit()

            # restart
            if ev.type == pg.KEYUP and ev.key == pg.K_F5:
                print("Attempting to restart (todo: not working)")
                game.init.quit(True)

            # print debug
            if ev.type == pg.KEYUP and ev.key == pg.K_F1:
                print("Logging debugger to a file.")
                game.utils.debug_append("F1")


class Update(Processor):

    def process(self):

        for obj in game.objects:
            obj.update()


class Draw(Processor):

    def process(self):
        _draw_lines()

        for obj in game.objects:
            obj.draw()


def _draw_lines():
    x0 = game.window_props.get_center().x
    y0 = game.window_props.get_center().y

    game.pygame.draw.line(game.window_surface, (0, 0, 0), (0, y0), (game.window_props.width, y0))
    game.pygame.draw.line(game.window_surface, (0, 0, 0), (x0, 0), (x0, game.window_props.width))

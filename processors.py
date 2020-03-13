import game
import random
import components as c

Processor = game.esper.Processor


# quit and stuff
class Events(Processor):

    def process(self):

        pg = game.pygame
        keys = game.loop.keys_pressed

        # alt-f4.
        # todo: this actually causes a fatal error which happens to be ok for now since that also quits the game.
        if keys[pg.K_F4] and keys[pg.KMOD_ALT]:
            game.init.quit()

        for ev in game.loop.events:

            # ui buttons (not implemented)
            if ev.type == pg.USEREVENT:
                if ev.user_type == 'ui_button_pressed':
                    pass
                    # if ev.ui_element == hello_button:
                    #     print('Hello World!')

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

            # 1: add a circle
            if ev.type == pg.KEYUP and ev.key == pg.K_1:
                game.populator.add_circles(1)

            # 2: delete a circle
            if ev.type == pg.KEYUP and ev.key == pg.K_2:
                game.populator.delete_circle()

            # 3: make all circles do stupid things
            if ev.type == pg.KEYUP and ev.key == pg.K_3:
                for circle in game.circle_things:
                    game.game_objects.GameObject.randomize_velocity(circle)


class Update(Processor):

    def process(self):

        for obj in game.objects:
            obj.update()


class Draw(Processor):

    def process(self):
        game.draw.draw()

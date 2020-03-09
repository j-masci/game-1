import game
import random
import components as c

_p = game.esper.Processor


# quit and stuff
class GameEvents(_p):

    def process(self):

        pg = game.pygame
        keys = game.loop.keys_pressed

        for ent, (tag, position, size) in game.world.get_components(c.UIComponent):
            pass

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


class GameObjectUpdates(_p):

    def process(self):
        game.player.update()


class PersonsHandler(_p):

    def process(self):

        for ent, (tag, position, size) in game.world.get_components(c.PersonTag, c.Position, c.Size):

            r = random.randint(0,100)

            if r > 40:

                r2 = random.randint(0, 100)
                r3 = random.randint(0, 100)
                r4 = random.randint(0, 100)

                position.x += 20 if r3 > 50 else -20
                position.y += 10 if r4 > 50 else -10

                # if r2 > 40:
                #     position.x += 20 if r3 > 50 else -20
                #
                # if r2 < 60:
                #     position.y += 10 if r3 > 50 else -10


class DrawMostThings(_p):

    def process(self):
        game.draw.draw()


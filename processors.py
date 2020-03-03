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

        # alt-f4
        if keys[pg.K_F4] and keys[pg.KMOD_ALT]:
            game.init.quit()

        for ev in game.loop.events:

            # ui buttons
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


class Stuff(_p):

    def process(self):

        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        if game.loop.keys_pressed[game.pygame.K_1]:
            game.player.position.x = game.window_props.get_center().x
            game.player.position.y = game.window_props.get_center().y

        if game.loop.keys_pressed[game.pygame.K_2]:
            game.player.size.height *= 2
            game.player.size.width *= 0.5

        if game.loop.keys_pressed[game.pygame.K_3]:
            game.player.size.height *= 0.7
            game.player.size.width *= 1.5

        if game.loop.keys_pressed[game.pygame.K_4]:
            game.player.size.height *= 0.9
            game.player.size.width *= 0.9

        if game.loop.keys_pressed[game.pygame.K_5]:
            if shift:
                game.populator._delete_random_person()
            else:
                game.populator._people(1)


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


# players event listeners
class PlayerHandler(_p):

    def process(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        # shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        if game.loop.keys_pressed[game.pygame.K_UP]:
            game.player.position.move_in_direction(10 if not space else 10, game.player.orientation.deg + 270)

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            game.player.position.move_in_direction(-10 if not space else -10, game.player.orientation.deg + 270)

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            game.player.orientation.deg += 6 if not space else 9

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            game.player.orientation.deg -= 6 if not space else 9


# draw things late
class DrawMostThings(_p):

    def process(self):
        game.draw.draw()


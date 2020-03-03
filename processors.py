import game

_p = game.esper.Processor


# players event listeners
class PlayerHandler(_p):

    def process(self):

        if game.loop.keys_pressed[game.pygame.K_UP]:
            game.player.position.move_in_direction(10, game.player.orientation.deg + 270)
            pass

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            game.player.position.move_in_direction(-5, game.player.orientation.deg + 270)
            pass

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            game.player.orientation.deg += 3
            pass

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            game.player.orientation.deg -= 3
            pass


# listen for quit and stuff
class TopLevelEventListener(_p):

    def process(self):

        pg = game.pygame

        for ev in game.loop.events:

            if ev.type == pg.QUIT:
                game.init.quit()

            # alt f4 (not working)
            if ev.type == pg.KEYUP and ev.key == pg.K_F4 and ev.mod is pg.KMOD_ALT:
                game.init.quit()

            # restart
            if ev.type == pg.KEYUP and ev.key == pg.K_F5:
                print("Attempting to restart (todo: not working)")
                game.init.quit(True)

            # print debug
            if ev.type == pg.KEYUP and ev.key == pg.K_F1:
                print("Logging debugger to a file.")
                game.utils.debug_append("F1")


# draw things late
class DrawMostThings(_p):
    def process(self):
        game.draw.draw()
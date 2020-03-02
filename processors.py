import game

_p = game.esper.Processor


# players event listeners
class PlayerHandler(_p):

    def process(self):
        pass

        # if self.app.loop.keys_pressed[pygame.K_UP]:
        #     self.app.player.position.move_in_direction(10, self.app.player.orientation.deg + 270)
        #     pass
        #
        # if self.app.loop.keys_pressed[pygame.K_DOWN]:
        #     self.app.player.position.move_in_direction(-5, self.app.player.orientation.deg + 270)
        #     pass
        #
        # if self.app.loop.keys_pressed[pygame.K_RIGHT]:
        #     self.app.player.orientation.deg += 3
        #     pass
        #
        # if self.app.loop.keys_pressed[pygame.K_LEFT]:
        #     self.app.player.orientation.deg -= 3
        #     pass


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
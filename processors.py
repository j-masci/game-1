from esper import esper
import pygame, components, funcs, sys, draw


# extend to accept app instance in constructor
class Processor(esper.Processor):

    def __init__(self, app):
        self.app = app
        pass


# players event listeners
class PlayerHandler(Processor):

    def process(self):

        if self.app.loop.keys_pressed[pygame.K_UP]:
            self.app.player.position.move_in_direction(10, self.app.player.orientation.deg + 270)
            pass

        if self.app.loop.keys_pressed[pygame.K_DOWN]:
            self.app.player.position.move_in_direction(-5, self.app.player.orientation.deg + 270)
            pass

        if self.app.loop.keys_pressed[pygame.K_RIGHT]:
            self.app.player.orientation.deg += 3
            pass

        if self.app.loop.keys_pressed[pygame.K_LEFT]:
            self.app.player.orientation.deg -= 3
            pass


# listen for quit and stuff
class TopLevelEventListener(Processor):

    def process(self):

        app = self.app

        for ev in app .loop.events:

            if ev.type == pygame.QUIT:
                app.quit()

            # alt f4 (not working)
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F4 and ev.mod is pygame.KMOD_ALT:
                app.quit()

            # restart
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F5:
                print("Attempting to restart (todo: not working)")
                app.quit(True)

            # print debug
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F1:
                print("Logging debugger to a file.")
                app.debug_append("F1")


# drawing is done late mostly
class DrawMostThings(Processor):

    def process(self):
        draw.draw(self.app)
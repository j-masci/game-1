from esper import esper
import pygame, components, funcs, sys


class PlayerHandler(esper.Processor):

    def process(self):

        if self.app.loop.keys_pressed[pygame.K_UP]:
            self.app.player.position.move_in_direction(10, self.app.player.orientation.deg + 270)
            pass

        if self.app.loop.keys_pressed[pygame.K_DOWN]:
            self.app.player.position.move_in_direction(-5, self.app.player.orientation.deg + 270)
            pass

        if self.app.loop.keys_pressed[pygame.K_RIGHT]:
            self.app.player.orientation.deg += 2
            pass

        if self.app.loop.keys_pressed[pygame.K_LEFT]:
            self.app.player.orientation.deg -= 2
            pass


class DrawMostThings(esper.Processor):
    def process(self):
        self.draw_player()
        self.draw_lines()

    def draw_player(self):
        player = self.app.player
        points = funcs.GetRect.via_object(player)
        pygame.draw.polygon(self.app.display, player.color.rgba(), points)

    def draw_lines(self):
        app = self.world.app
        pygame.draw.line(app.display, (0, 0, 0), (0, app.center.y), (app.size.x, app.center.y))
        pygame.draw.line(app.display, (0, 0, 0), (app.center.x, 0), (app.center.x, app.size.x))
        pass


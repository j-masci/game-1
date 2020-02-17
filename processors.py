from esper import esper
import pygame, components, funcs, sys


class PlayerHandler(esper.Processor):

    def process(self):
        for ev in self.app.loop.events:
            if ev.type is pygame.MOUSEMOTION:
                # print(ev)
                pass


class DrawMostThings(esper.Processor):
    def process(self):
        self.draw_player()
        self.draw_lines()

    def draw_player(self):
        player = self.app.player
        # player.orientation.deg += 1
        points = funcs.GetRect.via_object(player)
        pygame.draw.polygon(self.app.display, player.color.rgba(), points)

    def draw_lines(self):
        app = self.world.app
        pygame.draw.line(app.display, (0, 0, 0), (0, app.center.y), (app.size.x, app.center.y))
        pygame.draw.line(app.display, (0, 0, 0), (app.center.x, 0), (app.center.x, app.size.x))
        pass


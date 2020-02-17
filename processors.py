from esper import esper
import pygame
import components


class PlayerHandler(esper.Processor):

    def process(self):
        print(self.app.loop.count, self.app.loop.dt)
        for ev in self.app.loop.events:
            if ev.type is pygame.MOUSEMOTION:
                print(ev)


class DrawMostThings(esper.Processor):
    def process(self):
        self.draw_player()
        self.draw_lines()

    def draw_player(self):
        pos = self.world.component_for_entity(self.app.player, components.Position)
        pygame.draw.circle(self.app.display, (120,50,200), (pos.x, pos.y), 20)

    def draw_lines(self):
        app = self.world.app
        pygame.draw.line(app.display, (0, 0, 0), (0, app.center.y), (app.size.x, app.center.y))
        pygame.draw.line(app.display, (0, 0, 0), (app.center.x, 0), (app.center.x, app.size.x))
        pass


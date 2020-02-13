import sys, pygame
from Debugger import Debugger
from Timer import Timer
from Player import Player


class App:
    instance = None

    def __init__(self):

        self.instance = self

        self.clock = pygame.time.Clock()
        self.timer = Timer()
        self.debugger = Debugger()

        self.debugger.data.append({
            "app_init": 123
        })

        self.players = []
        self.players.append(Player(100, 100))

        self.loop_count = 0
        self.loop_count_last = 0
        self.is_paused = False

        pygame.init()

        self.size = pygame.Vector2(1440, 900)
        self.center = pygame.Vector2(int(self.size[0] / 2), int(self.size[1] / 2))

        self.display = pygame.display.set_mode((int(self.size.x), int(self.size.y)))
        self.loop()

    def draw(self):

        for player in self.players:
            player.draw(self.display)

        pygame.draw.line(self.display, (0, 0, 0), (0, self.center.y), (self.size.x, self.center.y))
        pygame.draw.line(self.display, (0, 0, 0), (self.center.x, 0), (self.center.x, self.size.x))

        # update the screen
        pygame.display.flip()
        self.clock.tick(10)

    def event(self, ev):

        if ev.type == pygame.QUIT:
            self.quit()
            return

        for player in self.players:
            player.event(ev, self)

        # print("Unhandled Event", ev.type, ev)

    def update(self):

        for player in self.players:
            player.update(self)

        pass

    def loop(self):

        while True:

            self.loop_count += 1

            for event in pygame.event.get():
                self.event(event)

            self.update()

            # reset everything from the last frame also
            self.display.fill((200, 100, 50))

            # draw all the things
            self.draw()

            # throttle to 60 fps
            pygame.time.Clock().tick(120)

    def quit(self):

        self.debug_snapshot()
        self.debugger.print()
        self.debugger.log()

        sys.exit()

    def debug_snapshot(self):

        self.debug_append("snapshot", {
            "loop_count": self.loop_count,
            "loop_count_last": self.loop_count_last,
            "is_paused": self.is_paused,
            "center": self.center
        })

    def debug_append(self, event, data=None):

        a = [event, self.timer.diff()]

        if data is not None:
            a.append(data)

        self.debugger.data.append(a)

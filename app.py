import sys, pygame, collections
from esper import esper
from debugger import Debugger
from timer import Timer
import processors, components


class App:
    instance = None

    def __init__(self):

        self.instance = self

        self.timer = Timer()
        self.debugger = Debugger()
        self.debug_append("app.init")

        # entity component system
        self.world = esper.World()
        self.world.app = self
        self.player = None

        self.loop = Loop()

        pygame.init()
        self.clock = pygame.time.Clock()

        self.size = pygame.Vector2(1440, 900)
        self.center = pygame.Vector2(int(self.size[0] / 2), int(self.size[1] / 2))

        self.display = pygame.display.set_mode((int(self.size.x), int(self.size.y)))

        # late-ish. may depend on world size.
        self.populate()

        self.do_loop()

    def populate(self):

        self.player = self.world.create_entity(*[
            components.Player(),
            components.Position(100, 100)
        ])

        self.add_processor(processors.PlayerHandler())
        self.add_processor(processors.DrawMostThings())

    def add_processor(self, processor):
        processor.app = self
        self.world.add_processor(processor)

    def get_player_components(self):
        return self.world.components_for_entity(self.player)

    def do_events(self):
        for ev in self.loop.events:
            if ev.type == pygame.QUIT:
                self.quit()

    def do_loop(self):

        while True:

            timer = Timer()

            times = collections.OrderedDict()

            self.loop.count += 1

            # gets and clears queued events
            self.loop.events = pygame.event.get()

            # ie. check quit. Other events likely handled within processors
            self.do_events()

            # reset the frame, before processors draw.
            self.display.fill((200, 100, 50))

            times["process_0"] = timer.time_since_last()

            # invoke registered processors
            self.world.process()

            times["process_1"] = timer.time_since_last()

            # updates the window with the new stuff
            pygame.display.flip()

            times["flip"] = timer.time_since_last()
            times["total_cpu"] = timer.time_since_start()

            # throttle updates per second
            self.loop.dt = pygame.time.Clock().tick(5)

            times["dt_1"] = timer.time_since_last()
            times["cpu_pct"] = times["dt_1"] / times["total_cpu"]

            self.debug_append("Loop # " + str(self.loop.count), times)

    def quit(self):

        self.debug_snapshot()
        self.debugger.print()
        self.debugger.log()

        sys.exit()

    def debug_snapshot(self):

        self.debug_append("snapshot", {
            "loop": self.loop,
            "center": self.center
        })

    def debug_append(self, event, data=None):

        a = [event, self.timer.time_since_start()]

        if data is not None:
            a.append(data)

        self.debugger.data.append(a)


# loop struct
class Loop:
    def __init__(self):
        self.count = 0
        self.dt = 0
        self.events = []


import sys, pygame, math, collections
import populator, components, processors, config, exceptions
from esper import esper
from debugger import Debugger
from timer import Timer


# the main app class that makes pretty much everything accessible.
# app.world is our ECS
class App:

    def __init__(self):

        self.timer = Timer()
        self.debugger = Debugger()
        self.debug_append("app.init")

        self.world = esper.World()
        self.extend_world_instance()

        self.loop = Loop()

        pygame.init()
        self.clock = pygame.time.Clock()

        self.size = components.IntegerPoint(config.display_size[0], config.display_size[1])
        self.center = pygame.Vector2(self.size.x/2, self.size.y/2)

        self.display = pygame.display.set_mode((self.size.x, self.size.y))

        # just before loop
        populator.populate(self)

        self.do_loop()

    def extend_world_instance(self):

        # give app to all processor instances
        # note: p.app.world === p.world
        def add_processor(p, pr):
            p.app = self
            self.world.add_processor(p, pr)

        self.world.add_processor = add_processor

    def do_loop(self):

        while True:

            timer = Timer()

            times = collections.OrderedDict()

            self.loop.count += 1

            # gets and clears queued events
            self.loop.events = pygame.event.get()
            self.loop.keys_pressed = pygame.key.get_pressed()

            # ie. check quit. Other events likely handled within processors
            self.do_events()

            # reset the frame, before processors draw.
            self.display.fill((200, 100, 50))

            times["process_0"] = timer.time_since_start()

            # invoke registered processors
            self.world.process()

            times["process_1"] = timer.time_since_start()

            # updates the window with the new stuff
            pygame.display.flip()

            times["total_cpu"] = timer.time_since_start()

            # throttle updates per second
            self.loop.dt = pygame.time.Clock().tick(config.updates_per_second)

            times["dt_1"] = timer.time_since_last()

            # need to keep this below 1
            times["cpu_pct"] = times["total_cpu"] / times["dt_1"]

            if config.track_times_in_loop:
                self.debug_append("Loop # " + str(self.loop.count), times)

    def quit(self, restart=False):

        self.debug_snapshot()
        # self.debugger.print()

        if config.debug_print_on_exit:
            self.debugger.print()

        if config.debug_log_on_exit:
            self.debugger.log()

        raise exceptions.QuitGameException("restart" if restart else "quit")

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


# some data that mutates on each loop iteration
class Loop:
    def __init__(self):
        self.count = 0
        self.dt = 0
        self.events = []
        self.keys_pressed = []

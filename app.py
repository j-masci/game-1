import sys, pygame, collections
from esper import esper
from debugger import Debugger
from timer import Timer
from Player import Player
import processors, components, config, exceptions


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
        self.player = Player()

        self.loop = Loop()

        pygame.init()
        self.clock = pygame.time.Clock()

        self.size = components.IntegerPoint(config.display_size[0], config.display_size[1])
        self.center = pygame.Vector2(self.size.x/2, self.size.y/2)

        self.display = pygame.display.set_mode((self.size.x, self.size.y))

        # late-ish. may depend on world size.
        self.populate()

        self.do_loop()

    def populate(self):

        # not really using ecs for the player, at least, not right now.
        self.player = Player()

        self.add_processor(processors.PlayerHandler())
        self.add_processor(processors.DrawMostThings())

    def add_processor(self, processor):
        processor.app = self
        self.world.add_processor(processor)

    def get_player_components(self):
        return self.world.components_for_entity(self.player)

    # do some top level event listening
    # most event listening is done within processes
    def do_events(self):
        for ev in self.loop.events:

            if ev.type == pygame.QUIT:
                self.quit()

            # alt f4 (not working)
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F4 and ev.mod is pygame.KMOD_ALT:
                self.quit()

            # restart
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F5:
                print("Attempting to restart (todo: not working)")
                self.quit(True)

            # print debug
            if ev.type == pygame.KEYUP and ev.key == pygame.K_F1:
                print("Logging debugger to a file.")
                self.debug_append("F1")

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


# loop struct
class Loop:
    def __init__(self):
        self.count = 0
        self.dt = 0
        self.events = []
        self.keys_pressed = []

import game, collections


def start():

    game.pygame.init()
    game.display = game.pygame.display.set_mode((game.window.width, game.window.height))
    game.populator.populate()

    while True:

        times = collections.OrderedDict()

        game.loop.count += 1

        # gets and clears queued events
        game.loop.events = game.pygame.event.get()
        game.loop.keys_pressed = game.pygame.key.get_pressed()

        # reset the frame, before processors draw.
        game.display.fill((200, 100, 50))

        times["process_0"] = game.timer.time_since_start()

        # invoke registered processors
        game.world.process()

        times["process_1"] = game.timer.time_since_start()

        # updates the window with the new stuff
        game.pygame.display.flip()

        times["total_cpu"] = game.timer.time_since_start()

        # throttle updates per second
        game.loop.dt = game.pygame.time.Clock().tick(game.config.updates_per_second)

        times["dt_1"] = game.timer.time_since_last()

        # need to keep this below 1
        times["cpu_pct"] = times["total_cpu"] / times["dt_1"]

        if game.config.track_times_in_loop:
            game.utils.debug_append("Loop # " + str(game.loop.count), times)


def quit(restart=False):

    if game.config.debug_print_on_exit:
        game.debugger.print()

    if game.config.debug_log_on_exit:
        game.debugger.log()

    raise game.exceptions.QuitGameException("restart" if restart else "quit")

import game, collections, os, pygame_gui, time


# starts the game
def start():
    game.pygame.init()

    # centers the window to be opened
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    date = time.strftime("%Y-%m-%d")

    game.pygame.display.set_caption("j-masci/game-1 | " + game.config.version + " | " + date)

    game.window_surface = game.pygame.display.set_mode((game.window_props.width, game.window_props.height))

    game.gui_manager = pygame_gui.UIManager((game.window_props.width, game.window_props.height))

    # add entities
    game.populator.populate()

    while True:

        times = collections.OrderedDict()

        def track(key, value):
            times[key] = value

        track("Test", 123)

        times = collections.OrderedDict()
        game.timer.time_since_last()

        game.loop.count += 1

        # gets and clears queued events
        game.loop.events = game.pygame.event.get()
        game.loop.keys_pressed = game.pygame.key.get_pressed()

        # reset the frame, before processors draw.
        game.window_surface.fill(game.config.background_color)

        # invoke registered processors
        game.world.process()

        times["process_1"] = game.timer.time_since_last()

        # updates the window with the new stuff
        game.pygame.display.flip()

        times["total_cpu"] = game.timer.time_since_last()

        # throttle updates per second
        game.loop.dt = game.clock.tick(game.config.updates_per_second)
        time_delta = game.loop.dt / 1000
        game.gui_manager.update(time_delta)
        game.gui_manager.draw_ui(game.window_surface)

        times["dt_1"] = game.timer.time_since_last()

        # need to keep this below 1
        times["cpu_pct"] = (times["total_cpu"] / times["dt_1"]) if times["dt_1"] > 0 else 0

        if game.config.track_times_in_loop:
            game.utils.debug_append("Loop # " + str(game.loop.count), times)


def quit(restart=False):
    if game.config.debug_print_on_exit:
        game.debugger.print()

    if game.config.debug_log_on_exit:
        game.debugger.log()

    raise game.exceptions.QuitGameException("restart" if restart else "quit")

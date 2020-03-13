import game, collections, os, pygame_gui, time, pprint


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

    # invisible mouse
    # game.pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
    game.pygame.mouse.set_visible(False)

    # font init
    game.pygame.font.init()

    while True:

        game.loop.count += 1

        timer = game.classes.Timer()
        times = collections.OrderedDict()

        # gets and clears queued events
        game.loop.events = game.pygame.event.get()
        game.loop.keys_pressed = game.pygame.key.get_pressed()

        # fill the background
        game.window_surface.fill(game.config.background_color)

        # update/draw
        game.world.process()

        game.on_screen_debugger.draw(game.window_surface)

        times["process_1"] = timer.time_since_start()

        # updates the window with the new stuff
        game.pygame.display.flip()

        end_time = timer.time_since_start()
        times["end_time"] = end_time

        # throttle updates per second
        game.loop.dt = game.clock.tick(game.config.updates_per_second)
        time_delta = game.loop.dt / 1000
        game.gui_manager.update(time_delta)
        game.gui_manager.draw_ui(game.window_surface)

        game.on_screen_debugger.state["frame_time"] = str(round(end_time * 100, 1)) + "ms"

        if game.config.track_times_in_loop:
            game.utils.debug_append("Loop # " + str(game.loop.count), times)


def quit(restart=False):
    if game.config.debug_print_on_exit:
        game.debugger.print()

    if game.config.debug_log_on_exit:
        game.debugger.log()

    raise game.exceptions.QuitGameException("restart" if restart else "quit")

import game


def populate():

    # entities
    add_circles(10)
    game.player = game.game_objects.Player()

    # processors
    game.world.add_processor(game.processors.Events())
    game.world.add_processor(game.processors.Update())
    game.world.add_processor(game.processors.Draw())


def add_circles(count):
    for i in range(0, count):
        game.circle_things.append(game.game_objects.CircleThingThatMoves())


def delete_circle():
    if game.circle_things:
        game.circle_things.pop(0)

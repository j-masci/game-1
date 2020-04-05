import game


def populate():

    # entities
    # add_circles(7)
    game.player = game.game_objects.Player()

    # game.objects.append(game.player)

    game.objects.append(game.temp.Thing())

    # processors
    game.world.add_processor(game.processors.Events())
    game.world.add_processor(game.processors.Update())
    game.world.add_processor(game.processors.Draw())


def add_circles(count):
    for i in range(0, count):
        game.objects.append(game.game_objects.CircleThingThatMoves())


def delete_circle():
    if game.circle_things:
        game.circle_things.pop(0)

import game
import components as c
import processors as p


def populate():
    _entities()
    _processors()


def _entities():
    _player_entity()


def _processors():

    def add(processor_instance, priority=0):
        game.world.add_processor(processor_instance, priority)

    add(p.TopLevelEventListener())
    add(p.PlayerHandler())
    add(p.DrawMostThings())


def _player_entity():
    game.world.create_entity(c.PlayerTag(), c.Position(50, 50), c.Orientation(90), c.Color(21, 11, 134), c.Size(30, 90))

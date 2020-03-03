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


# add player to ecs/world and to game module... 2 ways to access
# the same components, for now
def _player_entity():
    player = game.classes.Player()
    player.tag = c.PlayerTag()
    player.position = c.Position(50, 50)
    player.orientation = c.Orientation(90)
    player.color = c.Color(21, 11, 134)
    player.size = c.Size(30, 90)
    _e = game.world.create_entity
    player.entity_id = _e(player.tag, player.position, player.orientation, player.color, player.size)
    game.player = player

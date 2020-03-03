import random
import game
import components as c
import processors as p


def populate():
    _entities()
    _processors()


def _entities():
    _player_entity()
    _people(10)


def _processors():
    def add(processor_instance, priority=0):
        game.world.add_processor(processor_instance, priority)

    add(p.GameEvents())
    add(p.Stuff())
    add(p.PlayerHandler())
    add(p.PersonsHandler())
    add(p.DrawMostThings())


# add player to ecs/world and to game module... 2 ways to access
# the same components, for now
def _player_entity():
    player = game.classes.Player()
    player.tag = c.PlayerTag()
    player.position = c.Position(500, 500)
    player.orientation = c.Orientation(90)
    player.color = c.Color(21, 11, 134)
    player.size = c.Size(60, 20)
    _e = game.world.create_entity
    player.entity_id = _e(player.tag, player.position, player.orientation, player.color, player.size)
    game.player = player


def _delete_random_person():
    persons = []

    for ent, (person) in game.world.get_components(game.components.PersonTag):
        persons.append(ent)

    if len(persons) > 0:
        game.world.delete_entity(random.choice(persons))


def _people(how_many):
    for i in range(0, how_many):
        x = random.randint(0, game.window_props.width)
        y = random.randint(0, game.window_props.height)
        entity_id = game.world.create_entity(c.PersonTag(), c.Position(x, y), c.Size(random.randint(10, 20), 1),
                                             c.Color(random.randint(0, 255), random.randint(0, 255),
                                                     random.randint(0, 255)))
        print("person added", entity_id)

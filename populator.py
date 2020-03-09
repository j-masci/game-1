import random
import game
import components as c
import processors as p


# currently, the player object is not done in ECS because its
# only making it far more difficult right now. in the future
# maybe it will be. see game.player
def populate():
    _entities()
    _processors()


def _entities():
    _people(10)


def _processors():
    game.world.add_processor(p.GameEvents())
    game.world.add_processor(p.GameObjectUpdates())
    game.world.add_processor(p.PersonsHandler())
    game.world.add_processor(p.DrawMostThings())


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

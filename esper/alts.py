# exploring alternatives/variations to ecs

# say we have: person, enemies, bullets, trees, camera(s)

# i want the data oriented approach. composition over inheritance, and separation
# of data from behaviour. ok, so, does this mean we have to use ecs? there
# are other ways to use composition. perhaps, factories can work.
# how about functions that add components to entities. we'll
# try to keep components as only data. we have some things to
# figure out. if we construct a tree like object and give it
# a position component, how do we determine the initial position,
# and how do we give it a position in a way thats different
# from a human. maybe its just in 2 steps.
# step one is to add all components that an entity needs,
# step 2 would be to configure them I guess. configuring
# then in step 2 is kind of bullshit because we'll also
# configure them at every step of the loop. how do we organize
# these 2 very different but kind of similar operations.
# also, why do we even need factories. why can't we just construct
# a player object and use the constructor in a normal way.
# the play object can then be composed of as many components
# as we want. we can still try data oriented but surely it
# will feel very unnatural to move a function that belongs in
# the player entity to somewhere completely different.

def entity_draw_like_human(entity):
    def d():
        pass;

    entity.draw = d;


# what fucking purpose does this serve why not a fucking constructor?
def make_human():
    e = Entity()
    entity_draw_like_human(e)
    return e


class Entity:
    def __init__(self,id):
        self.id = id



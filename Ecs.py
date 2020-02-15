from dataclasses import dataclass


# use ecs??
# what are the goals?
# - avoid inheritance mess
# - separate data from behaviour ?
# - more pure-ish things ?

# update order problems
# loop through entities and do the things?
# loop through things and do the thing for each entity?
# no matter what, many loops, many potential ordering issues
# ecs says loop through processors, given priorities, then entities
# things of importance...
# keep things simple
# re-use code
# not re-strict flexibility
# pure functions are good
# don't actually need something super scalable. not building a big game
# performance also matters...
# keeping things simple and flexible should mean performance
# benefits at the cost of scalability.
# eventually, code will get more complex but shouldn't grow indefinitely
# scalability !== performance except maybe with a lot of time invested in optimization

# so 2 main things. the update loop, and the event listeners
# are these going to be separated or not? we can listen for events
# in the update loops. then events are handled within processes or processors

# maybe the simplest is approach is to not fit into any specific mold.
# how about, entities contain data and no behaviour. pure functions act on entities
# extremely simple... in a way. however, pure functions means passing around a lot
# of parameters. also, maybe pure is actually stupid for performance. a function should
# be able to mutate an object passed to it but we'll try to separate functions from data
# so that functions only act on their input, but they can still mutate that input

# how to link entities to components ?
# can entities just be IDs, literally, just int's?


def add_entity_to_component(entity_id, component):
    pass


def entity_component_del(entity_id, component):
    pass


# what is a system then... how does it work ...

class world:

    def __init__(self):
        self.entities = []

    def update(self):
        # well that's pretty simplistic.
        # not going to be good for ordering
        # unless, updates can queue things until later...
        for e in self.entities:
            e.update()

        pass


# one million decisions to make
# - do we call it Ecs or World? (ok that's not a hard decision)
# - does the Ecs store the relationship between components and entities or does
# it contain another object that stores those relationships?
# - how do we store the many to one rel? entity dict with array of comp, or the other way around, or both?
# - what kind of lookups do we have to do and how fast? is both an option? means data redundancy but
# also means we can lookup C via E or E via C and have it fast, except updating is slower.
# if entities are only IDs can we get away with using simple ints and not stupid classes that wrap an int
# do we even need classes for components or processors? is a component not just a name? and a system a callback?
# alternatively, we can have a component class that has a name and stores the list of entity IDs (i dont like this)
# do E, C, and S even try to work on their own? aren't they clearly tightly coupled to be useful?
# why would we have methods inside of the component or entity for setting/getting relationships? why would
# we ever want to do this outside of the context of Ecs? Perhaps, all methods go into Ecs.
# If all methods go into Ecs, can we just store primitive data types for E, C, and S
# doing so means far fewer lines of code and probably better efficiency. HOWEVER, storing
# primitive data types means no reference to an object, which sounds great for robust
# code, but is it good for efficiency? Will it not result in many copy by values to function
# calls?
# if we have classes for E, C, and S then we have a ton more shitty decisions to make
# do functions accept IDs or objects? now we need getters for both IDs and objects
# do the objects store their own IDs when the ID is also stored elsewhere like in a hash map or w/e
# basically, the same questions you run into every single time you create many objects with some unique IDs

class _Entity:
    def __init__(self, id):
        self.id = id

    def get_c(self):
        return []

    def set_c(self, c):
        pass


class Ecs:
    entities = []
    components = []
    systems = []

    def __init__(self):
        pass


class Entity:
    def __init__(self):
        pass


class System:
    def __init__(self):
        pass


class Component:
    def __init__(self):
        pass

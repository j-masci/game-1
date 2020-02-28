from esper import esper


class Processor(esper.Processor):
    pass


class World(esper.World):
    pass


# wanting to build my own but its a waste of time probably
# class EC:
#
#     def __init__(self):
#         self._entity_id = 0
#         self._component_id = 0
#         self._entities = []
#         self._components = []
#
#     def add_entity(self):
#         self._entity_id += 1
#         return self._entity_id
#
#     def add_component(self, entity_id, component_instance):
#         pass


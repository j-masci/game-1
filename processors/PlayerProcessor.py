from components import *
from esper import esper


class PlayerProcessor(esper.Processor):

    def process(self, dt):
        for ent, (player) in self.world.get_components(PlayerComponent):
            print("process player", ent)



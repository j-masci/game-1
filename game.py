# this is the god module, if that's a thing
import pygame, pygame_gui, sys
from esper import esper
import classes, config, utils, init, exceptions, components, processors, populator, draw

config = config
draw = draw
sys = sys
init = init
utils = utils
pygame = pygame
esper = esper
exceptions = exceptions
components = components
processors = processors
populator = populator
classes = classes
gui = pygame_gui
gui_manager = False
window_surface = False
window_props = classes.WindowProps(config.display_size[0], config.display_size[1])
clock = pygame.time.Clock()
debugger = classes.Debugger()
timer = classes.Timer()
loop = classes.Loop()
world = esper.World(config.ecs_timed)
player = False


def _get_components_vector(*component_types):

    ents = []

    for ent, components in world.get_components(*component_types):
        ents.append(ent, components)

    return ents


world.get_components_vector = _get_components_vector

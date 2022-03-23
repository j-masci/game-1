# a god module of sorts. rebelling against imports for some reason.
# instead of many imports you import just this and access everything.
# when this becomes too messy its going to be hell to re-factor. Oh well.
import pygame, pygame_gui, sys, math
from esper import esper
import classes, config, utils, init, exceptions, components, processors, populator, colors, random
import game_objects, mapping_functions, on_screen_debugger, temp

# rebelling against imports
config = config
random = random
sys = sys
temp = temp
math = math
init = init
utils = utils
pygame = pygame
esper = esper
colors = colors
exceptions = exceptions
components = components
processors = processors
populator = populator
on_screen_debugger = on_screen_debugger
classes = classes
mapping_functions = mapping_functions
gui = pygame_gui

window_props = classes.WindowProps(config.display_size[0], config.display_size[1])
clock = pygame.time.Clock()
debugger = classes.Debugger()
timer = classes.Timer()
loop = classes.Loop()
events = classes.Events()
world = esper.World(config.ecs_timed)
game_objects = game_objects
objects = []

# setup somewhere in start()
gui_manager = False
window_surface = False

# see populator.populate()
player = False
circle_things = []


def get_objects_of_instance(cls):
    return utils.filter_via_instance(objects, cls)

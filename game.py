# this is the god module, if that's a thing
import pygame, pygame_gui, sys, math
from esper import esper
import classes, config, utils, init, exceptions, components, processors, populator, draw, colors
import player as _player, mapping_functions

# rebelling against imports
config = config
draw = draw
sys = sys
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
classes = classes
mapping_functions = mapping_functions
gui = pygame_gui

window_props = classes.WindowProps(config.display_size[0], config.display_size[1])
clock = pygame.time.Clock()
debugger = classes.Debugger()
timer = classes.Timer()
loop = classes.Loop()
world = esper.World(config.ecs_timed)
player = _player.Player2()

# setup somewhere in start()
gui_manager = False
window_surface = False

import pygame, sys
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
# see init.start
display = False
window = classes.Window(config.display_size[0], config.display_size[1])
debugger = classes.Debugger()
timer = classes.Timer()
loop = classes.Loop()
world = esper.World(config.ecs_timed)
player = False

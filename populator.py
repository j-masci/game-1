import pygame, math, sys
import components as c
import processors as p
from esper import esper


def populate(app):
    _entities(app)
    _processors(app)


def _entities(app):
    _player_entity(app)


def _processors(app):

    def add(processor_instance, priority=0):
        app.world.add_processor(processor_instance, priority)

    # high priority runs first, default is zero
    add(p.TopLevelEventListener(app), 1000)
    add(p.PlayerHandler(app))
    add(p.DrawMostThings(app), -1000)


def _player_entity(app):
    app.world.create_entity(c.PlayerTag(), c.Position(50, 50), c.Orientation(90), c.Color(21, 11, 134), c.Size(30, 90))

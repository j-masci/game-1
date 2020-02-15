import sys, pygame
from esper import esper
from Debugger import Debugger
from Timer import Timer
from components import *
from processors import *


class App:
    instance = None

    def __init__(self):

        self.instance = self

        self.timer = Timer()
        self.debugger = Debugger()
        self.debug_append("app.init")

        # entity component system
        self.world = esper.World()
        self.player = None

        self.loop_count = 0
        self.loop_count_last = 0
        self.is_paused = False

        pygame.init()
        self.clock = pygame.time.Clock()

        self.size = pygame.Vector2(1440, 900)
        self.center = pygame.Vector2(int(self.size[0] / 2), int(self.size[1] / 2))

        self.display = pygame.display.set_mode((int(self.size.x), int(self.size.y)))

        # late-ish. may depend on world size.
        self.populate()

        self.loop()

    def populate(self):

        self.world.create_entity(*[PlayerComponent])

        self.world.add_processor(PlayerProcessor())

        pass

    def draw(self):

        pygame.draw.line(self.display, (0, 0, 0), (0, self.center.y), (self.size.x, self.center.y))
        pygame.draw.line(self.display, (0, 0, 0), (self.center.x, 0), (self.center.x, self.size.x))

        # update the screen
        pygame.display.flip()
        self.clock.tick(10)

    def event(self, ev):

        if ev.type == pygame.QUIT:
            self.quit()
            return

        # print("Unhandled Event", ev.type, ev)

    def update(self):

        self.world.process(2)

        pass

    def asdlkijasd(self):

        # update loop
        # 3 important things to do
        # handle events, update data, draw
        # events generally update data. are these 2 steps? is events first? same time?

        # ecs-ish
        # for all the things that things can do
        # get all the things that do the thing
        # and do the thing

        # naively update entities
        # for all the things that do things
        # do the things that the things do

        # second approach will have timing issues
        # does second approach lead to bad oop and much inheritance?
        # how to do the first approach but perhaps, not strictly ecs, or
        # with custom built ecs thats perhaps a bit more flexible


        # types of things vs. things to be done

        # ______, players, enemies, bullets, trees, watcher
        # move       1        1        1       0       0
        # die        1        1        0       0       0
        # explode    0        0        1       0       0
        # draw       1        1        1       1       0
        # events     1        0        0       0       1

        # I dont want to restrict anything.
        # it might make sense to perform all explode actions first,
        # and then later, all move actions, and finally, all draw actions
        # but, we might instead want to perform all actions on bullets first,
        # then continue performing other actions in order for all entities

        # so we have 2 main things to solve:
        # - avoid conflicts of order
        # - actions require specific inputs
        # a bullet explode action may require the positions of all trees to see
        # if the player or enemies will get hi.

        # its tempting to categorize entities by type. it seems logical,
        # but, actually very restrictive. Some things may have one and only
        # one logical "primary" type, but others might be purely a mix of 2 or more types,
        # with no logical way to choose just one. This is where ECS solves that,
        # we can still use tags to say, this entity is a bullet, but we must query
        # all bullets rather than storing entities in a single bullets array, where
        # a bullet must only be a bullet and cannot also be a projectile.
        # perhaps, when we want specific types, we can store entity IDs in our app,
        # no reason we can't have app.bullets, and inside some processor, get the bullets
        # like that. Then again is this not maybe just a total waste? Why not just use the
        # query system built into ECS which will not only have some caching but also probably
        # stores data in 2 places so it automatically knows all entities that are bullets.


        # if using ECS we have to figure some things out.
        # for example, where do we store the "thing" that draws a player specifically.
        # its so natural to want to add a draw method to a player entity, but the entity
        # is only an ID. Ok, so do we add a draw method to the player component? well,
        # i'm pretty sure that components are supposed to only hold the data. this is one
        # of the main purposes of ECS which is to not couple data with behaviour. processes
        # should do the behaviour. Ok, the only issue then is that to draw 20 different types
        # of entities don't we need 20 different systems? There's so many ways to do this. Do we
        # make an empty component tag called Drawable just in case we need to know which
        # entities are drawable in the first place? Do we then query all entities that are both
        # drawable AND players and then make a DrawPlayer process for it?
        # its really tempting to instead put the draw method inside of the component.
        # i'm sure that in theory this works. then we can have one draw process, the draw
        # process gets all entities that are Drawable, and invokes the dynamically defined
        # function held within the Drawable component. Again it seems backwards. All this bullshit
        # around ECS and data-driven blah blah blah and now we're putting behaviour into the component
        # instead? It just seems wasteful to define so many draw processes, one for every type of entity.
        # of course, there I go again, thinking about things in regards to types, which is almost impossible
        # to escape from. But regardless, if we have bullets, trees, and players, those are basically all
        # types and each of those types is going to be drawn in its own distinct way.
        # how many other things similar to drawing do we have to perform on different types of things.
        # perhaps we can do both. if a component has a draw function (as "data"), then draw it like that
        # actually, require the drawable component to be built with a draw function. If a component decides
        # to pass, it can do nothing. Then we can make a specific draw process for that component after.
        # this can be useful if the order in which we draw things are important. In fact, we might have
        # to be very careful to consider z-index especially in a 2d game. It's not a matter of change whether
        # to draw a person over top of a bullet or a bullet over top of a person.
        # anyways, we have an issue with this approach. The whole purpose of the system in my opinion
        # is that processes are the ones that have every single entity within scope. They are the ones that
        # determine what is required. So if we put 20 different types of draw functions inside of 20 draw
        # components (assigned to possibly much more than 20 entities), then how do we handle different draw
        # functions requiring different inputs? The single default draw process will have to invoke all draw
        # functions on components in the same way. This is perhaps why we need to have different draw processes
        # for different entity types.
        # ok so we would have to have a process called DrawLikeAPlayer, DrawLikeABullet, DrawLikeWhatever
        # again, this is a lot of processes, which is sort of what i'm trying to avoid. I hate the idea
        # of 1000 different classes with no structure behind them. {DoThing}LikeA{Thing} x 1000
        # that's why its so hard to escape from the stupid ways of oop thinking because at least
        # in oop it would {Thing}.{DoThing} which makes it way easier to find all the things that
        # players or bullets do. Nevertheless, we can still use a module approach or a static class
        # method approach to put things that players do inside of some place where its more logical,
        # but, we have to remember that things which are not players might still do things the same
        # way a player does. So inevitably, what happens when a process is identical for 2 completely
        # different types of things? Well this scenario is a piece of shit but its the same in OOP because
        # if you had a Player and a Bullet class and players and bullets did something identically then you
        # would still have no good place for that behaviour.

        # back to the table from above, the types of things and the things that are done.
        # in ECS, the two axes are not identical at all. The things done are the processes
        # and the types of things are the components (basically). Perhaps we can do better.
        # if you simply register all types of things and all the things that those should do,
        # then surely our global process has no job other than to run the process stored
        # in every single node of the matrix. But, the matrix itself can then also specify
        # when things are dependant on other things having been done first.
        # a simple priority system would be much simpler. Its then implicit. The programmer
        # has to know that if bullets explode at priority 50 then humans should not check
        # whether they are dead until at least 100. But it doesnt take a genius to know that this
        # can get too complex and run into serious issues. I would much rather declare the actions
        # that other actions depend on, whether they need to be done before or after.
        # if we properly declare all dependencies, then the processor can create a plan to
        # execute all things without violating any constraints.
        # (side note: this is where async operations may actually come in useful)
        # p.s. the processor may also have to keep track of which things are done on each iteration.
        # So.. this might be possible but definitely not without its challenges. Figuring
        # out the execution strategy might not turn out to be a serious issue on large data sets.
        # the execution strategy may have to be calculated upon register things and actions,
        # rather than upon starting a new iteration. However, processes themselves can certainly
        # add things and processes, causing the execution strategy to have to self adjust itself
        # and this could cause serious slowdown. For example, if we we say just once that
        # bullets have to explode before humans maybe die then this is fine but what if bullets
        # dont exist until a human shoots them and perhaps this constraint cannot be registered
        # early. However, perhaps we must register all types of actions that can possibly occur,
        # so that we know bullets have to explode first even if there are no bullets in the scene,
        # well, this means the dependency graph is no longer quite as dynamic as before.
        # curious to know, does a naive approach work for dependency resolution.
        # why don't we just start with the most obvious first cell, (0,0) or whatever the fuck
        # you want to call it. If it depends on other things, do those first, and if it doesnt
        # just fucking do the cell. I'm pretty sure there would be some similarities between
        # this approach and async processes. When an async process is encountered, it goes and
        # does the stupid thing and then when its done, comes back and continues (well, maybe,
        # I don't know).


        pass

    def loop(self):

        while True:

            self.loop_count += 1

            for event in pygame.event.get():
                self.event(event)

            self.update()

            # reset everything from the last frame also
            self.display.fill((200, 100, 50))

            # draw all the things
            self.draw()

            # throttle to 60 fps
            ms = pygame.time.Clock().tick(120)

    def quit(self):

        self.debug_snapshot()
        self.debugger.print()
        self.debugger.log()

        sys.exit()

    def debug_snapshot(self):

        self.debug_append("snapshot", {
            "loop_count": self.loop_count,
            "loop_count_last": self.loop_count_last,
            "is_paused": self.is_paused,
            "center": self.center
        })

    def debug_append(self, event, data=None):

        a = [event, self.timer.diff()]

        if data is not None:
            a.append(data)

        self.debugger.data.append(a)

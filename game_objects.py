import game, random


# and here we go with the inheritance already...
# exactly what i was trying to avoid.
class GameObject:

    __slots__ = ["position", "velocity", "acceleration", "size", "color", "orientation", "weight", "rotationalForce"]

    def update(self):
        pass

    def draw(self):
        pass

    @staticmethod
    def randomize_velocity(self, min=2, max=5):
        self.velocity.x = game.mapping_functions.maybe_negative(random.randint(min, max))
        self.velocity.y = game.mapping_functions.maybe_negative(random.randint(min, max))

    @staticmethod
    def resolve_rotation(self):
        self.orientation.degrees += self.rotationalForce.units

    @staticmethod
    def resolve_position(self):
        # doing the operation in this order is
        # called semi-implicit euler integration
        self.velocity += self.acceleration
        self.position += self.velocity

    @staticmethod
    def apply_rotational_dampening(self, step):
        self.rotationalForce.units = game.mapping_functions.approach_value(self.rotationalForce.units, 0, step)

    @staticmethod
    def apply_friction(self, step):
        pass
        self.velocity.x = game.mapping_functions.approach_value(self.velocity.x, 0, step)
        self.velocity.y = game.mapping_functions.approach_value(self.velocity.y, 0, step)

    @staticmethod
    def keep_on_screen(self):

        # its more fun if you augment the momentum, not dampen it
        multiplier = 1

        # primitive method for the time being, uses center position
        if self.position.x > game.window_props.width:
            self.velocity.x = -1 * multiplier * abs(self.velocity.x)

        if self.position.x < 0:
            self.velocity.x = multiplier * abs(self.velocity.x)

        if self.position.y > game.window_props.height:
            self.velocity.y = -1 * multiplier * abs(self.velocity.y)

        if self.position.y < 0:
            self.velocity.y = multiplier * abs(self.velocity.y)


class CircleThingThatMoves(GameObject):

    def __init__(self):

        r = game.random.randint

        width = r(10,20)
        self.size = game.components.Size(width, width)
        self.color = game.components.Color(r(0, 255), r(0, 255), r(0, 255))

        self.position = game.components.Position(r(0, game.window_props.width), r(0, game.window_props.height))
        self.velocity = game.components.Velocity()
        GameObject.randomize_velocity(self)
        self.acceleration = game.components.Acceleration(0, 0)

        self.weight = game.components.Weight(1)

    def draw(self):
        game.pygame.draw.circle(game.window_surface, self.color.rgba(), self.position.to_tuple(), int(self.size.width))

    def update(self):

        # before movement
        GameObject.apply_friction(self, 0.001)

        # movement
        GameObject.resolve_position(self)

        # after movement
        GameObject.keep_on_screen(self)


# player with momentum and rotational force
class Player(GameObject):

    def __init__(self):

        self.color = game.components.Color(100, 100, 250)
        self.size = game.components.Size(30, 60)

        self.orientation = game.components.Orientation(0)
        self.position = game.components.Position(500, 500)
        self.velocity = game.components.Velocity(0, 0)
        self.acceleration = game.components.Acceleration(0, 0)

        self.weight = game.components.Weight(1)
        self.rotationalForce = game.components.RotationalForce(0)

        self.points = []
        self.set_points()

    def set_points(self):
        self.points = game.utils.GetRect.via_object(self)

    def update(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]

        # before movement
        self.input()
        GameObject.apply_friction(self, 0.2 if space else 0.02)
        GameObject.apply_rotational_dampening(self, 0.3 if space else 0.03)

        # movement
        GameObject.resolve_rotation(self)
        GameObject.resolve_position(self)

        # after movement
        GameObject.keep_on_screen(self)

        # last
        self.set_points()

    def input(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        if game.loop.keys_pressed[game.pygame.K_BACKSPACE]:
            self.position.x = game.window_props.width / 2
            self.position.y = game.window_props.height / 2

        # apply rotational force
        # not right now
        if True:
            if game.loop.keys_pressed[game.pygame.K_a]:
                self.rotationalForce.units -= 1

            if game.loop.keys_pressed[game.pygame.K_d]:
                self.rotationalForce.units += 1

        # f: change direction
        for event in game.loop.events:
            if event.type == game.pygame.KEYDOWN:
                if event.key == game.pygame.K_f:
                    self.orientation.degrees += 90

        step = 1

        # apply momentum relative to orientation and arrow keys
        if game.loop.keys_pressed[game.pygame.K_UP]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 90)

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 270)

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            self.velocity.move_in_direction(step, self.orientation.degrees)

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 180)

    def draw(self):

        # the Player
        game.pygame.draw.polygon(game.window_surface, self.color.rgba(), self.points)

        # color the front of the rectangle
        game.pygame.draw.line(game.window_surface, game.colors.PINK, self.points[3], self.points[0], 8)

        # velocity vector
        game.pygame.draw.line(game.window_surface, game.colors.DARKSLATEBLUE, self.position,
                              self.position + self.velocity * 6, 3)

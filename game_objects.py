import game, random


# and here we go with the inheritance already...
# exactly what i was trying to avoid.
class GameObject:
    __slots__ = ["position", "velocity", "acceleration", "size", "color", "orientation", "weight", "rotationalForce",
                 "targetOrientation"]

    def update(self):
        pass

    def draw(self):
        pass

    @staticmethod
    def randomize_velocity(self, min=2, max=5):
        self.velocity.x = game.mapping_functions.maybe_negative(random.randint(min, max))
        self.velocity.y = game.mapping_functions.maybe_negative(random.randint(min, max))

    @staticmethod
    def resolve_orientation(self, speed):
        c = self.orientation.degrees
        t = self.targetOrientation.degrees
        self.orientation.degrees = game.components.Orientation.approach_value(c, t, speed)

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
    def shoot(self, rate, duration=1200):

        if self.can_shoot_at > game.loop.count:
            return

        self.can_shoot_at = game.loop.count + rate

        bullet = Bullet(duration)
        bullet.velocity = 0.5 * self.orientation.unit_vector()
        bullet.position = self.position.copy()
        game.objects.append(bullet)

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

    @staticmethod
    def keep_on_screen_circle(self):

        multiplier = 0.9

        # primitive method for the time being, uses center position
        if self.position.x + self.size.width > game.window_props.width:
            self.velocity.x = -1 * multiplier * abs(self.velocity.x)

        if self.position.x - self.size.width < 0:
            self.velocity.x = multiplier * abs(self.velocity.x)

        if self.position.y + self.size.width > game.window_props.height:
            self.velocity.y = -1 * multiplier * abs(self.velocity.y)

        if self.position.y - self.size.width < 0:
            self.velocity.y = multiplier * abs(self.velocity.y)


class CircleThingThatMoves(GameObject):

    def __init__(self):
        r = game.random.randint

        width = r(10, 20)
        self.size = game.components.Size(width, width)
        self.color = game.components.Color(r(0, 255), r(0, 255), r(0, 255))

        self.position = game.components.Position(r(0, game.window_props.width), r(0, game.window_props.height))
        self.velocity = game.components.Velocity()
        GameObject.randomize_velocity(self)
        self.acceleration = game.components.Acceleration(0, 0)

        self.weight = game.components.Weight(1)

    def draw(self):
        game.pygame.draw.circle(game.window_surface, self.color.rgba(), self.position.to_tuple_using_ints(),
                                int(self.size.width))

    def update(self):

        # before movement
        GameObject.apply_friction(self, 0.01)

        # movement
        GameObject.resolve_position(self)

        # after movement
        GameObject.keep_on_screen_circle(self)


class Explosion(GameObject):

    def __init__(self, pos):

        self.initial_width = 1
        self.size = game.components.Size(self.initial_width, self.initial_width)
        self.color = game.components.Color.random_instance()

        self.position = game.components.Position(pos)
        self.spawn_time = game.loop.count

        self.life = 0
        self.max_life = 60
        self.increment = 2

    def draw(self):
        if self.life >= 0:

            self.size.width = self.initial_width + self.life

            game.pygame.draw.circle(game.window_surface, self.color.rgba(), self.position.to_tuple_using_ints(),
                                    int(self.size.width))

    def update_life(self):
        if self.life < 0:
            return
        elif self.life is self.max_life:
            self.increment = -3
            self.life += self.increment
        else:
            self.life += self.increment

    def update(self):
        self.update_life()


class Bullet(GameObject):

    def __init__(self, duration=False):

        self.size = game.components.Size(6, 6)
        self.color = game.components.Color(255, 255, 255)
        self.position = game.components.Position(0, 0)
        self.velocity = game.components.Velocity()
        self.acceleration = game.components.Acceleration(0, 0)

        self.spawn_time = game.loop.count
        self.duration = duration

        self._dead = False

        # self.weight = game.components.Weight(1)

    @staticmethod
    def kill_all():
        for bullet in game.get_objects_of_instance(Bullet):
            if not bullet._dead:
                bullet._dead = True
                bullet.die()

    # on a scale of 0 to 1
    def how_dead(self):

        # very not dead
        if not self.duration:
            return 0

        # very dead
        if self.spawn_time + self.duration < game.loop.count:
            return 1

        # dying
        pct = (game.loop.count - self.spawn_time) / self.duration
        return min(1, pct)

    def is_alive(self):

        if self._dead:
            return False

        if not self.duration:
            return True

        return self.spawn_time + self.duration > game.loop.count

    def draw(self):

        if self.is_alive():

            shade_of_grey = int(self.how_dead() * 255)

            self.color.set(shade_of_grey, shade_of_grey, shade_of_grey)

            game.pygame.draw.circle(game.window_surface, self.color.rgba(), self.position.to_tuple_using_ints(),
                                    int(self.size.width))

    def die(self):
        expl = Explosion((self.position.x, self.position.y))
        game.objects.append(expl)
        pass

    def update(self):

        was_dead = self._dead

        if not self.is_alive():
            self._dead = True

            if not was_dead:
                self.die()

            return

        # GameObject.apply_friction(self, 0.1)

        # movement
        GameObject.resolve_position(self)

        # after movement
        GameObject.keep_on_screen_circle(self)


# player with momentum and rotational force
class Player(GameObject):

    def __init__(self):

        self.color = game.components.Color(100, 100, 250)
        self.size = game.components.Size(30, 60)

        self.orientation = game.components.Orientation(0)
        self.targetOrientation = game.components.Orientation(0)

        self.position = game.components.Position(500, 500)
        self.velocity = game.components.Velocity(0, 0)
        self.acceleration = game.components.Acceleration(0, 0)

        self.weight = game.components.Weight(1)
        self.rotationalForce = game.components.RotationalForce(0)

        self.can_shoot_at = 0

        self.points = []
        self.set_points()

    def set_points(self):
        self.points = game.utils.GetRect.via_object(self)

    def input(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]
        left_mouse = game.pygame.mouse.get_pressed()[0]
        right_mouse = game.pygame.mouse.get_pressed()[2]

        if left_mouse or space:
            GameObject.shoot(self, 2, 2000)

        if shift and right_mouse:
            Bullet.kill_all()

        for ev in game.loop.events_by_type(game.pygame.MOUSEMOTION):
            self.targetOrientation.degrees += int(ev.rel[0] * 0.45)
            # game.pygame.mouse.set_pos(game.window_props.get_center().x, game.window_props.get_center().y)

        if game.loop.keys_pressed[game.pygame.K_BACKSPACE]:
            self.position.x = game.window_props.width / 2
            self.position.y = game.window_props.height / 2

        if True:
            if game.loop.keys_pressed[game.pygame.K_a]:
                self.targetOrientation.degrees -= 1

            if game.loop.keys_pressed[game.pygame.K_d]:
                self.targetOrientation.degrees += 1

        # f: change direction
        for event in game.loop.events:
            if event.type == game.pygame.KEYDOWN:
                if event.key == game.pygame.K_f:
                    self.orientation.degrees += 180

        step = 0.1

        # apply momentum relative to orientation and arrow keys
        if game.loop.keys_pressed[game.pygame.K_UP]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 90)

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 270)

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            self.velocity.move_in_direction(step, self.orientation.degrees)

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            self.velocity.move_in_direction(step, self.orientation.degrees - 180)

    def update(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        # before movement
        self.input()

        if shift:
            GameObject.apply_friction(self, 0.1)

        # GameObject.apply_rotational_dampening(self, 0.3 if space else 0.03)

        # movement
        GameObject.resolve_orientation(self, 3)
        GameObject.resolve_rotation(self)
        GameObject.resolve_position(self)

        # after movement
        GameObject.keep_on_screen(self)

        game.on_screen_debugger.state["pos"] = self.position.to_tuple()
        game.on_screen_debugger.state["vel"] = self.velocity.to_tuple()
        game.on_screen_debugger.state["accel"] = self.acceleration.to_tuple()

        # last
        self.set_points()

    def draw(self):

        # the Player
        game.pygame.draw.polygon(game.window_surface, self.color.rgba(), self.points)

        # color the front of the rectangle
        game.pygame.draw.line(game.window_surface, game.colors.PINK, self.points[3], self.points[0], 8)

        # velocity vector
        game.pygame.draw.line(game.window_surface, game.colors.DARKSLATEBLUE, self.position,
                              self.position + 6 * self.velocity, 3)

        # target orientation
        game.pygame.draw.line(game.window_surface, game.colors.WHITE, self.position,
                              self.position + 500 * self.targetOrientation.unit_vector(), 3)

import game


# and here we go with the inheritance already...
# exactly what i was trying to avoid.
class GameObject:

    def update(self):
        pass

    def draw(self):
        pass


def reduce_plus_minus(units, step, threshold, below_threshold_return_value=0):

    ret = 0

    if units > threshold:
        ret = units - step
    elif units < threshold:
        ret = units + step

    return ret if abs(ret) > threshold else below_threshold_return_value


class Player(GameObject):
    __slots__ = ["position", "orientation", "size", "color"]

    # doing it like this is not going to be sufficient later on
    def set_points(self):
        self.points = game.utils.GetRect.via_object(self)

    def draw(self):
        points = game.utils.GetRect.via_object(self)
        game.pygame.draw.polygon(game.window_surface, self.color.rgba(), points)
        self.post_draw()

    def post_draw(self):
        pass


# player with momentum and rotational force
class Player2(Player):

    def __init__(self):

        self.color = game.components.Color(100, 100, 250)
        self.size = game.components.Size(30, 60)

        self.position = game.components.Position(500, 500)
        self.orientation = game.components.Orientation(0)

        self.momentum = game.components.Momentum(0, 0)
        self.rotationalForce = game.components.RotationalForce(0)
        self.weight = game.components.Weight(1)

        self.set_points()

    def apply_friction(self):

        if game.loop.keys_pressed[game.pygame.K_SPACE]:
            step_x = 1
            step_y = 1
        else:
            step_x = 0.01
            step_y = 0.01

        self.rotationalForce.units = reduce_plus_minus(self.rotationalForce.units, 0.1, 0.1)
        self.momentum.x = reduce_plus_minus(self.momentum.x, step_x, step_x)
        self.momentum.y = reduce_plus_minus(self.momentum.y, step_y, step_y)

    def input(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]
        step = 1

        if game.loop.keys_pressed[game.pygame.K_BACKSPACE]:
            self.position.x = game.window_props.width / 2
            self.position.y = game.window_props.height / 2

        # apply rotational force
        # not right now
        if False:
            if game.loop.keys_pressed[game.pygame.K_a]:
                self.rotationalForce.units -= 1

            if game.loop.keys_pressed[game.pygame.K_d]:
                self.rotationalForce.units += 1

        # simple rotation no forces for now
        if True:
            if game.loop.keys_pressed[game.pygame.K_a]:
                self.orientation.degrees -= 7

            if game.loop.keys_pressed[game.pygame.K_d]:
                self.orientation.degrees += 7

        # apply momentum relative to orientation and arrow keys
        if game.loop.keys_pressed[game.pygame.K_UP]:
            self.momentum.move_in_direction(step, self.orientation.degrees - 90)

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            self.momentum.move_in_direction(step, self.orientation.degrees - 270)

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            self.momentum.move_in_direction(step, self.orientation.degrees)

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            self.momentum.move_in_direction(step, self.orientation.degrees - 180)

    # for now, maybe rotation is more static
    def resolve_rotation(self):
        # self.orientation.degrees += 2 * self.rotationalForce.sigmoid(0.01)
        pass

    def resolve_momentum(self):

        if self.momentum.magnitude() > 0:
            self.position.x += self.momentum.x
            self.position.y += self.momentum.y

    # eventually we'll do something different here
    def keep_on_screen(self):

        multiplier = 0.5

        # doesn't actually always ensure the player stays on the screen
        if self.position.x > game.window_props.width:
            self.momentum.x *= - multiplier
            self.resolve_momentum()

        if self.position.x < 0:
            self.momentum.x *= - multiplier
            self.resolve_momentum()

        if self.position.y > game.window_props.height:
            self.momentum.y *= - multiplier
            self.resolve_momentum()

        if self.position.y < 0:
            self.momentum.y *= - multiplier
            self.resolve_momentum()

    def post_draw(self):

        # visual momentum vector
        game.pygame.draw.line(game.window_surface, game.colors.DARKSLATEBLUE, self.position,
                              self.position + self.momentum * 6, 3)

        # visual orientation vector
        game.pygame.draw.line(game.window_surface, game.colors.DARKGREEN, self.position,
                              self.position + self.orientation.unit_vector() * 30, 3)

        # color the front of the rectangle
        game.pygame.draw.line(game.window_surface, game.colors.PINK, self.points[3], self.points[0], 8)

    def update(self):
        self.input()
        self.keep_on_screen()
        self.apply_friction()
        self.resolve_momentum()
        self.resolve_rotation()

        # last
        self.set_points()


# old player object
# player with just a position and orientation basically
class Player1(Player):

    def __init__(self):
        self.color = game.components.Color(100, 100, 50)
        self.size = game.components.Size(30, 60)
        self.position = game.components.Position(500, 500)
        self.orientation = game.components.Orientation(0)

    def update(self):
        self.input()

    def input_movement(self):

        space = game.loop.keys_pressed[game.pygame.K_SPACE]
        # shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        if game.loop.keys_pressed[game.pygame.K_UP]:
            self.position.move_in_direction(10 if not space else 10, self.orientation.degrees + 270)

        if game.loop.keys_pressed[game.pygame.K_DOWN]:
            self.position.move_in_direction(-10 if not space else -10, self.orientation.degrees + 270)

        if game.loop.keys_pressed[game.pygame.K_RIGHT]:
            self.orientation.degrees += 6

        if game.loop.keys_pressed[game.pygame.K_LEFT]:
            self.orientation.degrees -= 6

    def input(self):

        shift = game.loop.keys_pressed[game.pygame.K_LSHIFT]

        if game.loop.keys_pressed[game.pygame.K_1]:
            self.position.x = game.window_props.get_center().x
            self.position.y = game.window_props.get_center().y

        if game.loop.keys_pressed[game.pygame.K_2]:
            self.size.height *= 2
            self.size.width *= 0.5

        if game.loop.keys_pressed[game.pygame.K_3]:
            self.size.height *= 0.7
            self.size.width *= 1.5

        if game.loop.keys_pressed[game.pygame.K_4]:
            self.size.height *= 0.9
            self.size.width *= 0.9

        if game.loop.keys_pressed[game.pygame.K_5]:
            if shift:
                game.populator._delete_random_person()
            else:
                game.populator._people(1)

import app
import sys

class Thing:

    def __init__(self):
        self.color = app.components.Color(20, 20, 220)
        self.points = []
        self.add_point()
        self.add_point()

    @staticmethod
    def random_point():
        return app.random.randint(400, 800), app.random.randint(400, 800)

    def add_point(self):
        self.points.append(self.random_point())

    def del_point(self):
        list.pop(self.points)

    def update(self):

        if app.events.key_up_occurred(None, app.pygame.K_1):
            self.add_point()

        if app.events.key_up_occurred(None, app.pygame.K_2):
            self.del_point()

    def draw(self):
        for x1, x2 in enumerate(self.points):

            app.pygame.draw.circle(app.window_surface, self.color.rgba(), x2, 5)

            for y1, y2 in enumerate(self.points):
                if x1 is not y1:
                    app.pygame.draw.line(app.window_surface, self.color.rgba(), x2, y2)




if False:

    def sq(func):

        print('dec')
        print(func.__code__.co_varnames)

        def ret(*args, **kwargs):

            print('invoke')
            print(args)
            print(kwargs)

            _args = []
            for v in args:
                _args.append(v*v)

            for k,v in kwargs.items():
                kwargs[k] = v*v

            return func(*_args, **kwargs)

        return ret


    @sq
    def asdf(x, y, z=123):
        print('asdf..')
        print(x)
        print(y)
        print(z)


    asdf(1,2,z=33)
    sys.exit()
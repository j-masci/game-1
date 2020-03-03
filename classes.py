import time, pprint, game


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_center(self):
        return game.components.Vector2(self.width / 2, self.height / 2)


# some data that mutates on each loop iteration
class Loop:
    def __init__(self):
        self.count = 0
        self.dt = 0
        self.events = []
        self.keys_pressed = []


class Player:
    __slots__ = ["entity_id", "tag", "position", "orientation", "color", "size"]


class Timer:

    def __init__(self, start_time=None):
        self._start_time = time.time() if start_time is None else start_time
        self._last_time = self._start_time

    # simply diffs given times. exists for possibly adding precision later.
    def diff_times(self, t0, t1):
        return t1 - t0

    # time between the time you pass in and now
    def time_since_given_time(self, t0):
        return self.diff_times(t0, time.time())

    # time between last call of this function, or class init, and now
    def time_since_last(self):
        now = time.time()
        ret = self.diff_times(self._last_time, now)
        self._last_time = now
        return ret

    # time between class init and now
    def time_since_start(self):
        return self.time_since_given_time(self._start_time)


class Debugger:

    def __init__(self):
        self.data = []
        self.pp = pprint.PrettyPrinter()

    def print(self):
        print("debugger...", self.data)

    def log(self):
        filename = "./logs/Debugger_" + str(int(time.time())) + ".txt"
        file = open(filename, "w")
        output = self.pp.pformat(self.data)
        file.write(output)
        file.close()

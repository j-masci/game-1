import time, pprint, game


class WindowProps:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_center(self):
        return game.components.Vector2(self.width / 2, self.height / 2)


class Events:
    def __init__(self):

        self.events = []
        self.keys_pressed = []
        self.key_down_events = []
        self.key_up_events = []

        pg = game.pygame

        self._key_mods = {
            "alt": pg.KMOD_ALT,
            "caps": pg.KMOD_CAPS,
            "ctrl": pg.KMOD_CTRL,
            "lalt": pg.KMOD_LALT,
            "lctrl": pg.KMOD_LCTRL,
            "lmeta": pg.KMOD_LMETA,
            "lshift": pg.KMOD_LSHIFT,
            "meta": pg.KMOD_META,
            "mode": pg.KMOD_MODE,
            "none": pg.KMOD_NONE,
            "num": pg.KMOD_NUM,
            "ralt": pg.KMOD_RALT,
            "rctrl": pg.KMOD_RCTRL,
            "rmeta": pg.KMOD_RMETA,
            "rshift": pg.KMOD_RSHIFT,
            "shift": pg.KMOD_SHIFT,
        }

        self._keys = {
            '0': pg.K_0,
            '1': pg.K_1,
            '2': pg.K_2,
            '3': pg.K_3,
            '4': pg.K_4,
            '5': pg.K_5,
            '6': pg.K_6,
            '7': pg.K_7,
            '8': pg.K_8,
            '9': pg.K_9,
            'a': pg.K_a,
            'ampersand': pg.K_AMPERSAND,
            'asterisk': pg.K_ASTERISK,
            'at': pg.K_AT,
            'b': pg.K_b,
            'backquote': pg.K_BACKQUOTE,
            'backslash': pg.K_BACKSLASH,
            'backspace': pg.K_BACKSPACE,
            'break': pg.K_BREAK,
            'c': pg.K_c,
            'capslock': pg.K_CAPSLOCK,
            'caret': pg.K_CARET,
            'clear': pg.K_CLEAR,
            'colon': pg.K_COLON,
            'comma': pg.K_COMMA,
            'd': pg.K_d,
            'delete': pg.K_DELETE,
            'dollar': pg.K_DOLLAR,
            'down': pg.K_DOWN,
            'e': pg.K_e,
            'end': pg.K_END,
            'equals': pg.K_EQUALS,
            'escape': pg.K_ESCAPE,
            'euro': pg.K_EURO,
            'exclaim': pg.K_EXCLAIM,
            'f': pg.K_f,
            'f1': pg.K_F1,
            'f10': pg.K_F10,
            'f11': pg.K_F11,
            'f12': pg.K_F12,
            'f13': pg.K_F13,
            'f14': pg.K_F14,
            'f15': pg.K_F15,
            'f2': pg.K_F2,
            'f3': pg.K_F3,
            'f4': pg.K_F4,
            'f5': pg.K_F5,
            'f6': pg.K_F6,
            'f7': pg.K_F7,
            'f8': pg.K_F8,
            'f9': pg.K_F9,
            'first': pg.K_FIRST,
            'g': pg.K_g,
            'greater': pg.K_GREATER,
            'h': pg.K_h,
            'hash': pg.K_HASH,
            'help': pg.K_HELP,
            'home': pg.K_HOME,
            'i': pg.K_i,
            'insert': pg.K_INSERT,
            'j': pg.K_j,
            'k': pg.K_k,
            'kp0': pg.K_KP0,
            'kp1': pg.K_KP1,
            'kp2': pg.K_KP2,
            'kp3': pg.K_KP3,
            'kp4': pg.K_KP4,
            'kp5': pg.K_KP5,
            'kp6': pg.K_KP6,
            'kp7': pg.K_KP7,
            'kp8': pg.K_KP8,
            'kp9': pg.K_KP9,
            'kp_divide': pg.K_KP_DIVIDE,
            'kp_enter': pg.K_KP_ENTER,
            'kp_equals': pg.K_KP_EQUALS,
            'kp_minus': pg.K_KP_MINUS,
            'kp_multiply': pg.K_KP_MULTIPLY,
            'kp_period': pg.K_KP_PERIOD,
            'kp_plus': pg.K_KP_PLUS,
            'l': pg.K_l,
            'lalt': pg.K_LALT,
            'last': pg.K_LAST,
            'lctrl': pg.K_LCTRL,
            'left': pg.K_LEFT,
            'leftbracket': pg.K_LEFTBRACKET,
            'leftparen': pg.K_LEFTPAREN,
            'less': pg.K_LESS,
            'lmeta': pg.K_LMETA,
            'lshift': pg.K_LSHIFT,
            'lsuper': pg.K_LSUPER,
            'm': pg.K_m,
            'menu': pg.K_MENU,
            'minus': pg.K_MINUS,
            'mode': pg.K_MODE,
            'n': pg.K_n,
            'numlock': pg.K_NUMLOCK,
            'o': pg.K_o,
            'p': pg.K_p,
            'pagedown': pg.K_PAGEDOWN,
            'pageup': pg.K_PAGEUP,
            'pause': pg.K_PAUSE,
            'period': pg.K_PERIOD,
            'plus': pg.K_PLUS,
            'power': pg.K_POWER,
            'print': pg.K_PRINT,
            'q': pg.K_q,
            'question': pg.K_QUESTION,
            'quote': pg.K_QUOTE,
            'quotedbl': pg.K_QUOTEDBL,
            'r': pg.K_r,
            'ralt': pg.K_RALT,
            'rctrl': pg.K_RCTRL,
            'return': pg.K_RETURN,
            'right': pg.K_RIGHT,
            'rightbracket': pg.K_RIGHTBRACKET,
            'rightparen': pg.K_RIGHTPAREN,
            'rmeta': pg.K_RMETA,
            'rshift': pg.K_RSHIFT,
            'rsuper': pg.K_RSUPER,
            's': pg.K_s,
            'scrollock': pg.K_SCROLLOCK,
            'semicolon': pg.K_SEMICOLON,
            'slash': pg.K_SLASH,
            'space': pg.K_SPACE,
            'sysreq': pg.K_SYSREQ,
            't': pg.K_t,
            'tab': pg.K_TAB,
            'u': pg.K_u,
            'underscore': pg.K_UNDERSCORE,
            'unknown': pg.K_UNKNOWN,
            'up': pg.K_UP,
            'v': pg.K_v,
            'w': pg.K_w,
            'x': pg.K_x,
            'y': pg.K_y,
            'z': pg.K_z,
        }

    # ie. update(pygame.events.get(), pygame.events.keys_pressed)
    def update(self, events, keys_pressed):

        self.events = events
        self.keys_pressed = keys_pressed
        self.key_up_events = []
        self.key_down_events = []

        for ev in events:

            if ev.type == game.pygame.KEYUP:
                self.key_up_events.append(ev.key)

            if ev.type == game.pygame.KEYDOWN:
                self.key_down_events.append(ev.key)

    def get_by_type(self, _type):
        return filter(lambda event: event.type == _type, self.events)

    def get_all(self):
        return self.events

    # for functions that allow string inputs or ints (ie. pygame constants)
    def map_key(self, key_str, key_int=None):

        if key_str is None and key_int is not None:
            return key_int

        return self._keys[key_str]

    # happens each frame when a key is held down
    def key_is_pressed(self, key_str, key_int=None):
        key = self.map_key(key_str, key_int)
        return True if self.keys_pressed[key] else False

    def key_up_occurred(self, key_str, key_int=None):
        key = self.map_key(key_str, key_int)
        return key in self.key_up_events

    # happens once per key press
    def key_down_occurred(self, key_str, key_int=None):
        key = self.map_key(key_str, key_int)
        return key in self.key_down_events


# some data that mutates on each loop iteration
class Loop:
    def __init__(self):
        self.count = 0
        self.dt = 0
        self.events = []
        self.keys_pressed = []

        self._keys_down = []
        self._keys_up = []

    def register_keys(self, events, keys_pressed):

        self.events = events
        self.keys_pressed = keys_pressed

        self._keys_down = []
        self._keys_up = []

        if events:

            for ev in events:
                print(ev)

            print(keys_pressed)

        for ev in events:

            if ev.type == game.pygame.KEYUP:
                self._keys_up.append(ev)

            if ev.type == game.pygame.KEYDOWN:
                self._keys_down.append(ev)

    # true if a key up event occurred on this frame (not if the key is "not down")
    def is_key_up(self, key):

        for ev in self._keys_up:
            if ev.key == key:
                return True

        return False

    def is_key_pressed(self, key):
        return True if self.keys_pressed[key] else False

    def is_key_down(self, key):

        for ev in self._keys_up:
            if ev.key == key:
                return True

        return False

    def events_by_type(self, type):

        def f(ev):
            return ev.type == type

        return filter(f, self.events)


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

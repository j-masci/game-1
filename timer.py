import time


class Timer:

    def __init__(self, start_time=None):
        self._start_time = time.time() if start_time is None else start_time
        self._last_time = self._start_time

    # simply diffs given times. exists for possibly adding precision later.
    def diff_times(self, t0, t1):
        return t1 - t0

    # time between the time you pass in and now
    def time_since_given_time(self, t0):
        return self.diff_times(time.time(), t0)

    # time between last call of this function, or class init, and now
    def time_since_last(self):
        now = time.time()
        ret = self.diff_times(self._last_time, now)
        self._last_time = now
        return ret

    # time between class init and now
    def time_since_start(self):
        return self.time_since_given_time(self._start_time)

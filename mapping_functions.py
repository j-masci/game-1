import math, sys


# maps (-infinity, infinity) to (-1, 1)
# or at least that's what i want it to do
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# rounds small or large values to -1 or 1
def sigmoid_rounded(x, error=0.03):
    return maybe_round_both_ways(sigmoid(x), -1, 1, error)


# rounding is perhaps not the best name for this
def maybe_round_up(value, limit, error):
    """
    >>> maybe_round_up(0.97, 1, 0.03)
    1
    >>> maybe_round_up(0.9, 1, 0.03)
    0.9
    """
    return value if value < limit - error else limit


def maybe_round_down(value, limit, error):
    """
    >>> maybe_round_down(-0.9, -1, 0.03)
    -0.9
    >>> maybe_round_down(-0.97, -1, 0.03)
    -1
    """
    return value if value > limit + error else limit


# ie. 0.99, -1, 1, 0.03 => 1
# ie. 0.95, -1, 1, 0.03 => 0.95
def maybe_round_both_ways(value, min, max, error):
    _value = maybe_round_down(value, min + error, min)
    _value = maybe_round_up(value, max - error, max)
    return _value

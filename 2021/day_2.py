
from functools import reduce

def get_input(day):
    inp = [x.split() for x in day.input]

    return [(k, int(v)) for k, v in inp]

def puzzle_1(day, *args, **kwargs):
    inp = get_input(day)

    return sum(v if k == 'down' else -v for k, v in inp if k in ('down', 'up')) * sum(v for k, v in inp if k == 'forward')

def puzzle_2(day, *args, **kwargs):
    inp = get_input(day)

    aim, depth = 0, 0
    hoz = 0

    for k, v in inp:
        if k == 'forward':
            hoz += v
            depth += aim * v
        elif k == 'up':
            aim -= v
        else:
            aim += v

    return hoz * depth

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

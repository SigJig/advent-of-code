
import math
from functools import reduce

def fuel(mass):
    return math.floor(mass / 3) - 2

def absolute_fuel(mass):
    f = fuel(mass)
    if f > 0:
        return f + absolute_fuel(f)

    return 0

def puzzle_1(day, *args, **kwargs):
    return reduce(lambda acc, x: acc + fuel(int(x)), day.input.readlines(), 0)

def puzzle_2(day, *args, **kwargs):
    return reduce(lambda acc, x: acc + absolute_fuel(int(x)), day.input.readlines(), 0)

if __name__ == '__main__':
    print(absolute_fuel(1969))

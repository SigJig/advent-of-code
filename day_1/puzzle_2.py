
import math
from functools import reduce

def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel > 0:
        return fuel + calculate_fuel(fuel)

    return 0

def main(day, puzzle, *args, **kwargs):
    return reduce(lambda acc, x: acc + calculate_fuel(x), puzzle.input, 0)

if __name__ == '__main__':
    print(calculate_fuel(1969))

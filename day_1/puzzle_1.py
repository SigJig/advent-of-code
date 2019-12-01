
import os
import math
import json
from functools import reduce

def main(day, puzzle, *args, **kwargs):
    return reduce(lambda acc, x: acc + math.floor(x / 3) - 2, puzzle.input, 0)

"""
https://adventofcode.com/2021/day/5
"""

from utils import pass_input
from dataclasses import dataclass
from typing import Tuple
from collections import defaultdict

@dataclass
class Line:
    frm: Tuple[int,int]
    to: Tuple[int,int]

    def __hash__(self):
        return hash(str(self))

def get_input(day):
    return [Line(*(tuple(map(int, y.split(','))) for y in x.split('->'))) for x in day.input]

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    """
    This is so slow lmfao
    """
    inp = (x for x in inp if not all(x.frm[i] != x.to[i] for i in range(2)))

    grid = defaultdict(int)
    intersections = 0

    for line in inp:
        dir_ = line.frm[0] == line.to[0]
        frm, to = line.frm[dir_], line.to[dir_]

        step = 1 if to > frm else -1
        for i in range(frm, to + step, step):
            point = (line.frm[0], i) if dir_ else (i, line.frm[1])
            grid[point] += 1

            if grid[point] == 2:
                intersections += 1

    return intersections#, sum(1 for x in grid for y in x.values() if y >= 2)

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    grid = defaultdict(int)
    intersections = 0

    for line in inp:
        diff_x, diff_y = (line.frm[i] != line.to[i] for i in range(2))
        step_x, step_y = (1 if line.to[i] > line.frm[i] else -1 for i in range(2))

        if diff_x:
            if not diff_y:
                step_y = 0

            rng = abs(line.frm[0] - line.to[0]) + 1
        else:
            step_x = 0
            rng = abs(line.frm[1] - line.to[1]) + 1

        for i in range(rng):
            point = (line.frm[0] + i * step_x, line.frm[1] + i * step_y)
            grid[point] += 1

            if grid[point] == 2:
                intersections += 1

    return intersections

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

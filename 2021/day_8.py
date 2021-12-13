"""
https://adventofcode.com/2021/day/8
"""

from utils import *

def get_input(day):
    return [[list(map(list, y.split())) for y in x.split('|')] for x in day.input]

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    return sum(sum(len(y) in (2, 4, 3, 7) for y in x[1]) for x in inp)

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    pass

@pass_input(get_input)
def puzzle_3(inp, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

@pass_input(get_input)
def puzzle_4(inp, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

"""
https://adventofcode.com/2021/day/7
"""

from utils import *
from collections import deque

def get_input(day):
    return [int(x) for x in day.input.read().split(',')]

def gauss(start, stop):
    """
    https://stackoverflow.com/questions/20455977/sum-up-all-the-integers-in-range
    """
    return (stop - start) * (start + stop - 1) // 2

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    possibles = list(range(min(inp), max(inp) + 1))

    return min(sum(abs(x - y) for y in inp) for x in possibles)

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    possibles = list(range(min(inp), max(inp) + 1))

    return min(sum(gauss(0, abs(x - y) + 1) for y in inp) for x in possibles)

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

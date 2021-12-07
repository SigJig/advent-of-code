"""
https://adventofcode.com/2021/day/7
"""

from utils import *

def get_input(day):
    return [int(x) for x in day.input.read().split(',')]

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    res = []
    for iidx, i in enumerate(inp):
        res.append(0)
        for jidx, j in enumerate(inp):
            if iidx == jidx:
                continue

            res[iidx] += abs(j - i)

    return min(res)

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    res = []
    mn, mx = min(inp), max(inp)
    for iidx, i in enumerate(range(mn,mx+1)):
        res.append(0)
        for jidx, j in enumerate(inp):            
            res[iidx] += sum(range(abs(j - i) + 1))

    return min(res)

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

"""
https://adventofcode.com/2021/day/6
"""

from utils import pass_input
from collections import deque

def get_input(day):
    return [int(x) for x in day.input.read().split(',')]

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    days = 80
    dq = deque([days+6-num for num in inp])
    total = len(inp)

    while dq:
        x = dq.popleft()

        if x < 7:
            continue

        direct = x // 7
        dq.extend([x - (7 * n + 9) for n in range(direct)])
        total += direct

    return total

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    # Yeah that challenged should be considered a crime against humanity
    pass

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

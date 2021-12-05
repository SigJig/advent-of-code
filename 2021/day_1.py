"""
https://adventofcode.com/2021/day/1
"""

import sys
import itertools
from collections import deque

def get_input(day):
    return (int(x.strip()) for x in day.input)

def puzzle_1(day, *args, **kwargs):
    """
    O(n) time, O(1) memory
    """
    inc = 0
    inp = get_input(day)
    last = next(inp)

    for num in inp:
        if num > last:
            inc += 1

        last = num

    return inc

def puzzle_2(day, *args, **kwargs):
    dq = deque()
    inp = get_input(day)

    for _ in range(3): dq.append(next(inp))
    last = sum(dq)

    inc = 0

    for i in inp:
        dq.popleft()
        dq.append(i)

        s = sum(dq)

        if s > last:
            inc += 1

        last = s

    return inc

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions

    This is straight from reddit, only here to benchtest
    Faster
    O(n) time, O(n) memory
    """
    nums = list(get_input(day))

    return sum(x < y for x, y in zip(nums, nums[1:]))

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    
    Faster
    O(n) time, O(1) memory
    """

    dq = deque()
    inp = get_input(day)

    for _ in range(3): dq.append(next(inp))
    
    #print(f'{(sys.getsizeof(dq) + sys.getsizeof(inp)) / 1024}kb')
    inc = 0

    for i in inp:
        inc += dq.popleft() < i
        dq.append(i)
    
    return inc

def puzzle_5(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions

    This is straight from reddit, only here to benchtest.
    
    
    
    
    it's faster. fuck you. i hat e u cunt why is this faster its not fair this uses like a bunch more memory :(
    
    O(n) time, O(n) memory
    """
    nums = list(get_input(day))
    #print(f'{sys.getsizeof(nums, nums[3:]) / 1024}kb')

    return sum(x < y for x, y in zip(nums, nums[3:]))

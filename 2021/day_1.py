
from collections import deque
from functools import reduce

def get_input(day):
    return (int(x.strip()) for x in day.input.readlines())

def puzzle_1(day, *args, **kwargs):
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

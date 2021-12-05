"""
https://adventofcode.com/2021/day/4
"""

def get_input(day):
    lines = (x for x in day.input if x.strip())
    seq = (int(x) for x in next(lines).split(','))

    boards = []
    dict_ = {}
    for idx, line in enumerate(lines):
        # For every board, create:
        # - Dictionary containing number on board as key, and (xvalue, yvalue) as value
        # - List for sum of marked numbers on every x
        # - List for sum of marked numbers on every y
        dict_.update({int(num): (idx % 5, yidx) for yidx, num in enumerate(line.split())})

        if (idx + 1) % 5 == 0:
            boards.append((dict_.copy(), ([0] * 5, [0] * 5)))
            dict_ = {}

    return seq, boards

def sort_winners(seq, boards):
    queue = []
    found = set()

    for num in seq:
        for idx, (board, (sums_x, sums_y)) in enumerate(boards):
            if idx not in found and ((pos := board.pop(num, None)) is not None):
                x, y = pos
                sums_x[x] += 1
                sums_y[y] += 1

                if sums_x[x] >= 5 or sums_y[y] >= 5:
                    queue.append(sum(board.keys()) * num)
                    found.add(idx)

    return queue


def puzzle_1(day, *args, **kwargs):
    return sort_winners(*get_input(day))[0]

def puzzle_2(day, *args, **kwargs):
    return sort_winners(*get_input(day))[-1]

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """


from functools import reduce
from operator import __lt__, __ge__

def get_input(day, *args, **kwargs):
    return [int(x, 2) for x in day.input]

def puzzle_1(day, *args, **kwargs):
    inp = get_input(day)
    overflow = [0] * 11

    for i in inp:
        for idx in range(len(overflow) - 1, -1, -1):
            overflow[idx] += 1 if (i & 1) else -1
            i >>= 1

    bits = reduce(lambda x, y: (x << 1) | (0 if y <= 0 else 1), overflow, 0)
 
    return bits * (bits ^ 0xfff)

def puzzle_2(day, *args, **kwargs):
    def find(inp, more=True):
        comp = __ge__ if more else __lt__
        shifts = 11

        while len(inp) > 1 and shifts >= 0:
            zeros, ones = [], []
            for i in inp:
                is_one = i & (1 << shifts)

                if is_one:
                    ones.append(i)
                else:
                    zeros.append(i)

            shifts -= 1
            inp = ones if comp(len(ones), len(zeros)) else zeros

        return inp[0]

    inp = get_input(day)

    return find(inp, True) * find(inp, False)

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

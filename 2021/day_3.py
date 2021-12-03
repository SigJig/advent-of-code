
from functools import reduce
from operator import __lt__, __ge__

def get_input(day, *args, **kwargs):
    data = [int(x, 2) for x in day.input]

    return data, max(x.bit_length() for x in data)

def puzzle_1(day, *args, **kwargs):
    inp, bc = get_input(day)
    overflow = [0] * bc

    for i in inp:
        for idx in range(len(overflow) - 1, -1, -1):
            overflow[idx] += 1 if (i & 1) else -1
            i >>= 1

    bits = reduce(lambda x, y: (x << 1) | (0 if y <= 0 else 1), overflow, 0)
 
    return bits * (bits ^ 0xfff)

def puzzle_2(day, *args, **kwargs):
    def find(inp, bc, more=True):
        comp = __ge__ if more else __lt__
        shifts = bc - 1

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

    inp, bc = get_input(day)

    return find(inp, bc, True) * find(inp, bc, False) # oxygen * co2

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    
    Pulled from reddit: https://www.reddit.com/r/adventofcode/comments/r7r0ff/comment/hn1biw9/?utm_source=share&utm_medium=web2x&context=3

    Faster, as the counting is done with the sum function
    """
    data, bits = get_input(day)
    gamma = 0

    for i in range(bits):
        gamma_bit = sum((x >> i) & 1 for x in data) > len(data) // 2
        gamma |= gamma_bit << i

    return gamma * (2 ** bits - 1 ^ gamma)

from collections import Counter
def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    
    Pulled from reddit: https://www.reddit.com/r/adventofcode/comments/r7r0ff/comment/hn17b24/?utm_source=share&utm_medium=web2x&context=3

    The fact that this is faster is extremely infuriating (but makes sense)
    """
    data = [x for x in day.input.read().strip().split('\n')]

    ll = data

    theta = ''
    epsilon = ''
    for i in range(len(ll[0])):
        common = Counter([x[i] for x in ll])

        if common['0'] > common['1']:
            ll = [x for x in ll if x[i] == '0']
        else:
            ll = [x for x in ll if x[i] == '1']
        theta = ll[0]

    ll = data
    for i in range(len(ll[0])):
        common = Counter([x[i] for x in ll])

        if common['0'] > common['1']:
            ll = [x for x in ll if x[i] == '1']
        else:
            ll = [x for x in ll if x[i] == '0']
        if ll:
            epsilon = ll[0]

    return (int(theta,2)*int(epsilon,2))

def puzzle_5(day, *args, **kwargs):
    """
    Pulled from: https://www.reddit.com/r/adventofcode/comments/r7r0ff/comment/hn1biw9/?utm_source=share&utm_medium=web2x&context=3
    
    Slower :DDDDD
    """
    data, bits = get_input(day)

    o2, co2 = [*data], [*data]

    for i in range(bits - 1, -1, -1):
        o2_bit = sum((x >> i) & 1 for x in o2) >= len(o2) / 2
        o2 = [x for x in o2 if (x >> i) & 1 == o2_bit] or o2

    for i in range(bits - 1, -1, -1):
        co2_bit = sum((x >> i) & 1 for x in co2) < len(co2) / 2
        co2 = [x for x in co2 if (x >> i) & 1 == co2_bit] or co2

    return o2[0] * co2[0]
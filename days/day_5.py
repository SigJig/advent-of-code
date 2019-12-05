
from .lib.intcode import intcode

def get_input(day):
    return list(map(int, day.input.read().split(',')))

def puzzle_1(day, *args, **kwargs):
    inp = get_input(day)
    outs = []
    
    intcode(inp, iter([1]), outs)

    return outs[-1]

def puzzle_2(day, *args, **kwargs):
    inp = get_input(day)
    outs = []

    intcode(inp, iter([5]), outs)

    return outs

if __name__ == '__main__':
    outs = []
    intcode([3,9,7,9,10,9,4,9,99,-1,8], iter([8]), outs)

    print(outs)
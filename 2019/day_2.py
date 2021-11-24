
from .lib.intcode import intcode

def get_input(day):
    return list(map(int, day.input.read().split(',')))

def puzzle_1(day, *args, **kwargs):
    data = get_input(day)
    data[1], data[2] = 12, 2

    return intcode(data)[0]

def puzzle_2(day, result=None, *args, **kwargs):
    data = get_input(day)

    if result is None:
        raise Exception('Missing arguments')
    else:
        result = int(result)

    for i in range(100):
        for j in range(100):
            tmp = data[:]
            tmp[1], tmp[2] = i, j

            if intcode(tmp)[0] == result:
                return 100 * i + j

    raise Exception('FUCK')

if __name__ == '__main__':
    print(intcode([2,4,4,5,99,0]))

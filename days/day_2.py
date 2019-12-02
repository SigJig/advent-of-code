
from operator import add, mul

opcodes = [add, mul] 

def intcode(sequence):
    iterator = iter(sequence)

    for x in iterator:
        if x in (1, 2):
            left, right, value = (next(iterator) for _ in range(3))

            operator = opcodes[x-1]

            sequence[value] = operator(*map(sequence.__getitem__, (left, right)))
        elif x == 99:
            return sequence
        else:
            raise Exception(f'Unrecognized opcode {x}')

    raise Exception(f'Unexpected EOL')

def get_input(day):
    return list(map(int, day.input.read().split(',')))

def puzzle_1(day, *args, **kwargs):
    data = get_input(day)
    data[1], data[2] = 12, 2

    return intcode(data)

def puzzle_2(day, *args, **kwargs):
    data = get_input(day)

    for i in range(100):
        for j in range(100):
            tmp = data[:]
            tmp[1], tmp[2] = i, j

            if intcode(tmp)[0] == 19690720:
                return 100 * i + j

    raise Exception('FUCK')

if __name__ == '__main__':
    print(intcode([2,4,4,5,99,0]))

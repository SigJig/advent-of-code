
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
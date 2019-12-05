
from operator import add, mul, lt, eq

def param_type(params, arg_num):
    return (params >> arg_num) & 1

def parse_opcode(opcode):
    return opcode % 100, int(str(opcode // 100), 2)

def get_real_val(seq, params, val, index=0):
    return val if param_type(params, index) else seq[val]

class OpcodesIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self._iter = iter(self.sequence)

    def iter_set(self, idx):
        self._iter = iter(self.sequence)

        for _ in range(idx): next(self)

        return self

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._iter)

    def opcodes(self):
        for x in self.__iter__():
            yield parse_opcode(x)

    def next(self, amt=1):
        return (next(self) for _ in range(amt))

def intcode(sequence, inputs=None, out=[]):
    it = OpcodesIterator(sequence)

    for opcode, params in it.opcodes():
        if opcode in (1, 2):
            args = list(it.next(3))

            left, right = (get_real_val(sequence, params, x, index) for index, x in enumerate(args[:2]))
            mem_place = args[-1]

            operator = [add, mul][opcode-1]

            sequence[mem_place] = operator(left, right)
        elif opcode in (3, 4):
            if opcode == 3:
                assert param_type(params, 0) == 0

                sequence[next(it)] = next(inputs)
            else:
                out.append(get_real_val(sequence, params, next(it)))
        elif opcode in (5, 6):
            check_is_true = opcode == 5

            value, mem_place = (get_real_val(sequence, params, x, index) for index, x in enumerate(it.next(2)))

            # Do an extra iteration to skip to the next
            if (bool(value) == check_is_true): it.iter_set(mem_place)
        elif opcode in (7, 8):
            operator = [lt, eq][opcode - 7]

            num, cmp, mem_place = it.next(3)
            num, cmp = (get_real_val(sequence, params, x, index) for index, x in enumerate([num, cmp]))

            sequence[mem_place] = int(operator(num, cmp))
        elif opcode == 99:
            return sequence
        else:
            raise Exception(f'Unrecognized opcode {opcode}')

    raise Exception(f'Unexpected EOL')
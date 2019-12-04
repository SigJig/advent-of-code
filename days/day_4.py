
class NumLowerException(Exception): pass

def iter_num(num):
    last = 0

    for char in iter(str(num)):
        digit = int(char)

        if digit < last: raise NumLowerException()
        yield last, digit

        last = digit

def get_input(day):
    return map(int, day.input.read().split('-'))

def puzzle_1(day, *args, **kwargs):
    start, end = get_input(day)
    amt = 0

    for i in range(start, end):
        it = iter_num(i)

        try:
            for last, digit in it:
                if last == digit:
                    for _ in it: pass

                    raise StopIteration
        except NumLowerException:
            pass
        except StopIteration:
            amt += 1    

    return amt

def puzzle_2(day, *args, **kwargs):
    start, end = get_input(day)
    amt = 0

    for i in range(start, end):
        it = iter_num(i)
        incr = 0

        try:
            for last, digit in it:
                if last == digit:
                    incr += 1
                else:
                    if incr == 1:
                        for _ in it: pass
                    else:
                        incr = 0
            else:
                if incr == 1: amt += 1
        except (StopIteration, NumLowerException):
            pass

    return amt
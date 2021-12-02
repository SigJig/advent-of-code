
import os
import re
from pathlib import Path
from utils import Day
from time import perf_counter

class Color:
    data = {
        'HEADER': '\033[95m',
        'OKGREEN': '\033[0;32;40m',
        'OKYELLOW': '\033[0;33;40m',
        'OKPURP': '\033[0;35;40m',
        'OKCYAN': '\033[0;36;40m',
        'WARNING': '\033[94m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    @classmethod
    def format(cls, message, color):
        return cls.data[color.upper()] + message + cls.data['ENDC']

class CLI:
    def __init__(self, sys_args):
        self.sys_args = sys_args
        self.main()

    def parse_args(self):
        options = {}
        args = []

        iterator = iter(self.sys_args)

        for arg in iterator:
            if arg.startswith('-'):
                try:
                    options[arg.lstrip('-')] = next(iterator)
                except StopIteration:
                    raise Exception(Color.format(f'Missing value for {arg}', 'FAIL'))
            else:
                args.append(arg)

        return args, options

    def main(self):
        args, options = self.parse_args()
        command = args[0]

        try:
            f = getattr(self, command)
        except AttributeError:
            raise Exception('Unrecognized command ' + command)
        else:
            return f(*args[1:], **options)

    def _get_year(self, options):
        if (year := options.pop('year', None)) is None:
            years = sorted((x for x in Path(__file__).parent.iterdir() if re.match(r'\d{4}', str(x)) and x.is_dir()), reverse=True)

            try:
                return years[0]
            except IndexError:
                print(Color.format(f'No years available', 'FAIL'))
                return None
        
        return year

    def _get_day(self, *args, **options):
        if (year := self._get_year(options)) is None:
            raise Exception(Color.format('No day specified', 'FAIL'))
        
        return Day(int(args[0]), year)

    def make(self, *args, **options):
        if len(args) < 1 or not args[0].isdigit():
            pass

        return self._get_day(*args, **options).make()

    def bench(self, *args, **options):
        day = self._get_day(*args, **options)
        cycles = int(options.pop('cycles', 10000))

        start = perf_counter()
        for _ in range(cycles):
            day.run(*args[1:], **options)

        print(Color.format(f'Benched at {cycles} iterations: {round(perf_counter()-start, 5)}s', 'OKGREEN'))


    def run(self, *args, **options):
        if (year := self._get_year(options)) is None:
            return None

        day = Day(int(args[0]), year)
        data = day.run(*args[1:], **options)

        puzzle = options.get('puzzle', None)

        if not puzzle:
            colors = ['OKGREEN', 'OKYELLOW', 'OKPURP', 'OKCYAN']

            for index, i in enumerate(data):
                result, time = i

                print(Color.format(
                    f'Puzzle {index + 1}: {result} ({time}s)',
                    colors[index % (len(colors))]))
        else:
            result, time = data[0]

            print(Color.format(f'Puzzle returned {result} ({time}s)', 'OKCYAN'))

if __name__ == '__main__':
    import sys

    CLI(sys.argv[1:])
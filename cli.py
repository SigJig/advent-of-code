
import os
from utils import Day

class Color:
    data = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
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
                options[arg.lstrip('-')] = next(iterator)
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

    def make(self, *args, **options):
        day = Day(int(args[0]))

        if puzzle := options.get('puzzle', None):
            return day.puzzle(int(puzzle)).make()

        return day.make()

    def run(self, *args, **options):
        day = Day(int(args[0]))

        puzzle = options.get('puzzle', None)
        data = day.run(options.get('puzzle', None))

        if not puzzle:
            colors = ['OKGREEN', 'OKBLUE']

            for index, i in enumerate(data):
                print(Color.format(f'Puzzle {index + 1}: {i}', colors[index]))
        else:
            print(Color.format('Puzzle returned ' + str(data), 'OKBLUE'))

if __name__ == '__main__':
    import sys

    CLI(sys.argv[1:])
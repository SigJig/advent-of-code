
import os
import re
from functools import reduce
from importlib import import_module

class DayExists(Exception):
    def __init__(self, day, *args, **kwargs):
        message = f'Day {day} already exists'

        super().__init__(message, *args, **kwargs)

class Day:
    def __init__(self, day):
        self.day = day

        self.basename = f'day_{self.day}'
        self.path = os.path.join(self.__class__.days_dir(), self.basename + '.py')
        self.input_path = os.path.join(self.__class__.input_dir(), self.basename + '.txt')

    def __int__(self):
        return self.day

    def _import(self):
        try:
            return import_module('.' + self.basename, 'days')
        except ImportError as e:
            raise ImportError(f'Unable to import day {int(self.day)}, puzzle {int(self)}') from e

    def run_puzzle(self, puzzle, *args, **kwargs):
        attr = self.puzzle_basename(puzzle)

        try:
            module = self._import()

            method = getattr(module, attr)
        except AttributeError as e:
            raise AttributeError(f'Imported module does not have a {attr} method') from e

        return method(self, *args, **kwargs)

    def run(self, puzzle=None, *args, **kwargs):
        if puzzle is not None:
            return self.run_puzzle(puzzle, *args, **kwargs)

        module = self._import()

        return [getattr(module, method)(self, *args, **kwargs) for method in filter(lambda x: re.match(r'^puzzle_\d+$', x), dir(module))]

    def make(self):
        if os.path.exists(self.path):
            raise DayExists(self.day)

        if not os.path.exists(self.input_dir()):
            os.mkdir(self.input_dir())

        with open(self.path, 'w+') as fp:
            template = '''
            def {0}(day, *args, **kwargs):
                pass

            def {1}(day, *args, **kwargs):
                pass
            '''.split('\n')

            template = '\n'.join([x.replace(' ' * 4 * 3, '') for x in template])

            fp.write(template.format(*[self.puzzle_basename(x) for x in [1, 2]]))

        with open(self.input_path, 'w+') as inp: pass

    def puzzle_basename(self, puzzle):
        return f'puzzle_{puzzle}'

    @property
    def input(self):
        return open(self.input_path)

    @classmethod
    def all_days(cls):
        for root, _, files in os.walk(cls.days_dir()):
            for file in files:
                if re.match(r'^day_\d+\.py$', file): yield os.path.join(root, file)

    @classmethod
    def days_dir(cls):
        return os.path.join(os.path.dirname(__file__), 'days')

    @classmethod
    def input_dir(cls):
        return os.path.join(cls.days_dir(), 'input')

if __name__ == '__main__':
	print(len(list(Day.all_days())), list(Day.all_days()))

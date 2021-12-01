
import os
import re
import time
from functools import reduce
from importlib import import_module

class DayExists(Exception):
    def __init__(self, day, *args, **kwargs):
        message = f'Day {day} already exists'

        super().__init__(message, *args, **kwargs)

class Day:
    def __init__(self, day, year):
        self.day = day
        self.year = str(year)

        self.basename = f'day_{self.day}'
        self.path = os.path.join(self.__class__.days_dir(year), self.basename + '.py')
        self.input_path = os.path.join(self.__class__.input_dir(year), self.basename + '.txt')

    def __int__(self):
        return self.day

    def _import(self):
        try:
            return import_module('.' + self.basename, self.year)
        except ImportError as e:
            raise ImportError(f'Unable to import day {int(self.day)}, puzzle {int(self)}') from e

    def run_method(self, method, *args, **kwargs):
        start = time.perf_counter()
        result = method(self, *args, **kwargs)

        return result, round(time.perf_counter() - start, 8)

    def run(self, *args, **kwargs):
        module = self._import()

        if 'puzzle' in kwargs:
            methods = [self.puzzle_basename(x) for x in kwargs.pop('puzzle').split()]
        else:
            methods = filter(lambda x: re.match(r'^puzzle_\d+$', x), dir(module))

        return [self.run_method(getattr(module, method), *args, **kwargs) for method in methods]

    def make(self):
        if os.path.exists(self.path):
            raise DayExists(self.day)

        if not os.path.exists(self.input_dir(self.year)):
            os.mkdir(self.input_dir(self.year))

        with open(self.path, 'w+') as fp:
            template = '''
            def {0}(day, *args, **kwargs):
                pass

            def {1}(day, *args, **kwargs):
                pass
            '''.split('\n')

            template = '\n'.join([x.replace(' ' * 4 * 3, '') for x in template])

            fp.write(template.format(*[self.puzzle_basename(x) for x in range(1,3)]))

        with open(self.input_path, 'w+') as inp: pass

    def puzzle_basename(self, puzzle):
        return f'puzzle_{puzzle}'

    @property
    def input(self):
        return open(self.input_path)

    @classmethod
    def all_days(cls, year):
        for root, _, files in os.walk(cls.days_dir(year)):
            for file in files:
                if re.match(r'^day_\d+\.py$', file): yield os.path.join(root, file)

    @classmethod
    def days_dir(cls, year):
        return os.path.join(os.path.dirname(__file__), year)

    @classmethod
    def input_dir(cls, year):
        return os.path.join(cls.days_dir(year), 'input')

if __name__ == '__main__':
	print(len(list(Day.all_days())), list(Day.all_days()))

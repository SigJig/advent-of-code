
import os
import re
import json
import requests
from functools import reduce
from importlib import import_module

class DayExists(Exception):
    def __init__(self, day, *args, **kwargs):
        message = f'Day {day} already exists'

        super().__init__(message, *args, **kwargs)

class Day:
    def __init__(self, day):
        self.day = day
        self.puzzles = set()

        self.dir_basename = f'day_{self.day}'
        self.path = os.path.join(self.__class__.days_dir(), self.dir_basename)
        self.input_dir = os.path.join(self.path, 'input')

    def __int__(self):
        return self.day

    def puzzle(self, puzzle):
        for i in self.puzzles:
            if getattr(i, 'puzzle') == puzzle:
                return i

        pzl = Puzzle(puzzle, self)
        self.puzzles.add(pzl)

        return pzl

    def run(self, puzzle=None):
        if puzzle is not None:
            return self.puzzle(int(puzzle)).run()

        return [x.run() for x in self.puzzles]

    def make_dirs(self):
        if os.path.exists(self.path):
            raise DayExists(self.day)

        os.mkdir(self.path)
        os.mkdir(self.input_dir)

        with open(os.path.join(self.path, '__init__.py'), 'w+') as fp: pass

    def make(self):
        for i in range(1, 3): self.puzzle(i).make()

    @classmethod
    def all_days(cls):
        return [
            os.path.join(root, file) for root, file in (
                files for root, files, folders in os.walk(cls.days_dir)
            )
        ]

    @classmethod
    def num_days(cls):
        return reduce(lambda acc, x: acc + x, cls.all_days(), 0)

    @classmethod
    def days_dir(cls):
        return os.path.join(os.path.dirname(__file__))

class Puzzle:
    def __init__(self, puzzle, day):
        self.puzzle = puzzle
        self.day = day

    def __int__(self):
        return self.puzzle

    def run(self, *args, **kwargs):
        try:
            module = import_module(f'.{self.puzzle_basename}', self.day.dir_basename)

            main = getattr(module, 'main')
        except ImportError as e:
            raise ImportError(f'Unable to import day {int(self.day)}, puzzle {int(self)}') from e
        except AttributeError as e:
            raise AttributeError(f'Imported module does not have a `main` method') from e

        return main(self.day, self, *args, **kwargs)

    def make(self):
        try:
            self.day.make_dirs()
        except DayExists:
            pass

        with open(os.path.join(self.day.path, self.python_file), 'w+') as fp:
            template = '''
            def main(day, puzzle, *args, **kwargs):
                pass
            '''.split('\n')

            template = '\n'.join([x.replace(' ' * 4 * 3, '') for x in template])

            fp.write(template.format(day=int(self.day), puzzle=int(self)))

        with open(os.path.join(self.day.input_dir, self.input_file), 'w+') as fp: pass

    @property
    def input(self):
        with open(os.path.join(self.day.input_dir, self.input_file)) as fp:
            return json.load(fp)

    @property
    def puzzle_basename(self):
        return f'puzzle_{self.puzzle}'

    @property
    def input_file(self):
        return self.puzzle_basename + '.json'

    @property
    def python_file(self):
        return self.puzzle_basename + '.py'
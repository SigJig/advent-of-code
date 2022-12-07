
import functools
from dataclasses import dataclass

INDENT_MULT = 4

@dataclass
class File:
    path: str
    size: int

    def __str__(self):
        return f'{self.size} {self.path}'

@dataclass
class Directory:
    path: str
    children: list
    files: list
    parent: 'Directory'

    def __str__(self):
        return f'dir {self.path}'

    def print_dir(self, indent=0):
        for x in self.children:
            print(f'{" " * indent * INDENT_MULT}{str(x)}')
            x.print_dir(indent+1)

        for x in self.files:
            print(f'{" " * indent * INDENT_MULT}{str(x)}')

    def size(self):
        return sum(x.size for x in self.files) + sum(x.size() for x in self.children)

class Fs:
    def __init__(self):
        self.root = Directory("/", [], [], None)
        self.cwd = self.root
        self.results_reader = None

    def cd(self, path, *args):
        if path.startswith("/"):
            last = self.root
            path = path[1:]
        elif path.startswith(".."):
            self.cwd = self.cwd.parent
            return self.cd(path[2:])
        else:
            last = self.cwd

        for p in path.split("/"):
            if not p.strip():
                continue

            last.children.append(Directory(
                p, [], [], last
            ))

            last = last.children[-1]

        self.cwd = last

    def _list(self, result):
        result = result.split(" ")
        if result[0] == "dir":
            if result[1] not in [x.path for x in self.cwd.children]:
                #self.cwd.children.append(
                #    Directory(result[1], [], [], self.cwd)
                #)
                pass
        else:
            self.cwd.files.append(File(result[1], int(result[0])))

    def ls(self, *args):
        self.results_reader = self._list

    def resolve_cmd(self, args):
        self.results_reader = None
        getattr(self, args[0])(*args[1:])

    def resolve_read(self, result):
        self.results_reader(result)

def main():
    with open('r2022/input/day_7.txt') as fp:
        inp = fp.read()

    fs = Fs()

    for line in inp.split("\n"):
        if line.startswith('$ '):
            fs.resolve_cmd(line[2:].split(' '))
        else:
            fs.resolve_read(line)
    
    work = [fs.root]
    required = 30e6 - (70e6 - fs.root.size())
    smallest = (None, 70e6)
    sum_ = 0
    while work:
        x = work.pop()

        xsum = x.size()
        if xsum <= 100000:
            sum_ += xsum
        if xsum >= required and xsum < smallest[1]:
            smallest = (x, xsum)

        work.extend(x.children)

    print(f'sum: {sum_}')
    print(f'smallest: ({str(smallest[0])}, {smallest[1]}) (root size: {fs.root.size()})')

if __name__ == '__main__':
    main()

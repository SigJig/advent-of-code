"""
https://adventofcode.com/2021/day/6
"""

import sys
from utils import pass_input
from collections import deque

def get_input(day):
    return [int(x) for x in day.input.read().split(',')]

class Cache:
    def __init__(self, days):
        self.days = days
        self._cache = {}

    def __getitem__(self, item):
        return self.get(item)

    def get(self, num):
        if num in self._cache:
            return self._cache[num]

        try:
            tot = self.calc(num)
        except RecursionError:
            return 0
        self._cache[num] = tot

        return tot

    def get_shifted(self, num):
        # Days + 6 - num gives us the amount of days the fish has lived for
        return self.get(self.days + 6 - num)

    def bulk(self, bulk):
        return len(bulk) + sum(self.get_shifted(x) for x in bulk)

    def calc(self, num):
        # If less than 0, a new fish has not been created
        if num < 7: return 0

        # Fish are created every 7 days.
        # This tells us how many this particular fish has directly created in its life
        total = direct = num // 7

        for i in range(direct):
            # When a new fish is created, it creates a new one 9 days after
            # The nth fish created will then have the age of its parent - 7 * n
            # Then we subtract 9, as it does not create new fish in the first 9 days
            tmp = num - 7*i - 9

            if tmp > 0:
                total += self.get(tmp)

        return total

@pass_input(get_input)
def puzzle_1(inp, *args, **kwargs):
    """
    Can use the puzzle 2 solution with cli argument --days 80
    """
    days = 80
    # Days + 6 - num gives us the amount of days the fish has lived for
    dq = deque([days + 6 - num for num in inp])
    total = len(inp)

    while dq:
        fish_life = dq.popleft()

        # If less than 0, a new fish has not been created
        if fish_life < 7:
            continue

        # Fish are created every 7 days.
        # This tells us how many this particular fish has directly created in its life
        direct = fish_life // 7

        # When a new fish is created, it creates a new one 9 days after
        # The nth fish created will then have the age of its parent - 7 * n
        # Then we subtract 9, as it does not create new fish in the first 9 days
        dq.extend([fish_life - (7 * n + 9) for n in range(direct)])
        total += direct

    return total

@pass_input(get_input)
def puzzle_2(inp, *args, **kwargs):
    cache = Cache(int(kwargs.get('days', 80)))
    result = cache.bulk(inp)

    print(f'Cache size at: {sys.getsizeof(cache._cache) / 1024}KB')

    return result

def puzzle_3(day, *args, **kwargs):
    """
    Optimizations for puzzle 1 after having looked at other peoples solutions
    """

def puzzle_4(day, *args, **kwargs):
    """
    Optimizations for puzzle 2 after having looked at other peoples solutions
    """

from functools import total_ordering
from itertools import permutations


@total_ordering
class NamedHeight:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height

    def __hash__(self):
        return self.height

class Solution:

    def __init__(self, *args):
        self._all = args
        for arg in args:
            setattr(self, arg.name, arg) #creating attributes many of them

    def correct(self):
        try:
            return all((
                self.W > self.D,
                self.W < self.Z,
                self.L > self.B,
                self.L < self.D,
                self.L < self.W,
                self.B != min(self._all)
            ))
        except AttributeError:
            return False

    def __str__(self):
        return ' | '.join(
            f'{c.name} {c.height}' for c 
            in sorted(self._all, reverse=True))

class SolutionFactory:

    def __init__(self, names):
        self.names = names

    def create(self, heights):
        args = [NamedHeight(n, h) for n, h in
                zip(self.names, heights)]
        return Solution(*args)

    def __iter__(self):
        return (self.create(hs) for hs in
                permutations(range(len(self.names))))

factory = SolutionFactory(
    ['W', 'D', 'Z', 'L', 'B', 'K'])
for solution in factory:
    if solution.correct():
        print(solution)







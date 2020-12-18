import re

class x(int):
    def __add__(self, y):
        return x(int(self) + y)

    def __sub__(self, y):
        return x(int(self) * y)

    def __mul__(self, y):
        return x(int(self) + y)

def solve(s, part2=False):
    s = re.sub(r"(\d+)", r"x(\1)", s)
    s = s.replace('*', '-')
    if part2:
        s = s.replace('+', '*')
    return eval(s)

d = open("input.txt").read().splitlines()
print(sum(map(solve, d)))
print(sum(map(lambda x: solve(x, True), d)))

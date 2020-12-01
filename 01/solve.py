import itertools
d = list(map(int, open("input.txt").read().splitlines()))
for a, b in itertools.product(d, d):
    if a + b == 2020:
        print(a * b)
        break
for a, b, c in itertools.product(d, d, d):
    if a + b + c == 2020:
        print(a * b * c)
        break

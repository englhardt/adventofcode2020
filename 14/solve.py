import itertools
from collections import defaultdict

d = open("input.txt").read().splitlines()

# Part 1
mem = defaultdict(int)
m, mf = 0, 0
t_m = str.maketrans('X01', '100')
t_mf = str.maketrans('X01', '001')
for l in d:
    x = l.split(' = ')
    if 'mask' in l:
        m, mf = [int(x[1].translate(t), 2) for t in [t_m, t_mf]]
    elif 'mem' in l:
        mem[int(x[0][4:-1])] = m & int(x[1]) | mf
print(sum(mem.values()))

# Part 2
mem = defaultdict(int)
m, mf = 0, 0
t_mf = str.maketrans('X01', '011')
for l in d:
    x = l.split(' = ')
    if 'mask' in l:
        m, mf = x[1], int(x[1].translate(t_mf), 2)
    elif 'mem' in l:
        for comb in itertools.product('01', repeat=m.count('X')):
            cur_m = m
            for v in comb:
                cur_m = cur_m.replace('X', v, 1)
            mem[int(cur_m, 2) | int(x[0][4:-1]) & mf] = int(x[1])
print(sum(mem.values()))

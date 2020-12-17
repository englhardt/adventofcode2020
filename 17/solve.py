import copy
from collections import defaultdict

def num_neighbors(g, x, y, z, w, p2=False):
    n = -g[(x, y, z, w)]
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2) if p2 else [0]:
                    n += g[(i, j, k, l)]
    return n

def evolve(g, p2=False):
    g_new = copy.deepcopy(g)
    lb = list(map(min, zip(*g.keys())))
    ub = list(map(max, zip(*g.keys())))
    for i in range(lb[0] - 1, ub[0] + 2):
        for j in range(lb[1] - 1, ub[1] + 2):
            for k in range(lb[2] - 1, ub[2] + 2):
                for l in range(lb[3] - 1, ub[3] + 2) if p2 else [0]:
                    p = (i, j, k, l)
                    n = num_neighbors(g, *p, p2)
                    if g[p] and n not in [2, 3]:
                        g_new[p] = False
                    elif not g[p] and n == 3:
                        g_new[p] = True
    return g_new

def sim(g, p2=False):
    for _ in range(6):
        g_new = evolve(g, p2)
        g = g_new
    return g

d = open("input.txt").read().splitlines()
g = defaultdict(lambda: False)
for y in range(len(d)):
    for x in range(len(d[y])):
        g[(x, y, 0, 0)] = d[y][x] == '#'
print(sum(sim(g, False).values()))
print(sum(sim(g, True).values()))

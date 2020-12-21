import numpy as np
from collections import defaultdict
from operator import itemgetter
import itertools

def calc_borders(x):
    return [''.join(x[0, :]), ''.join(x[-1, :]), ''.join(x[:, 0]), ''.join(x[:, -1])]

def flip_rot(x):
    b = []
    for k in range(4):
        xr = np.rot90(x, k=k)
        b.append(xr)
        for a in [0, 1]:
            xf = np.flip(xr, axis=a)
            b.append(xf)
    return b

d = open("input.txt").read().split('\n\n')[:-1]
d = {int(x[5:9]): np.array([[x for x in y] for y in x[11:].splitlines()]) for x in d}

borders = {}
for i, x in d.items():
    borders[i] = set()
    for xf in flip_rot(x):
        borders[i].update(calc_borders(xf))

nb = defaultdict(list)
for i, j in itertools.combinations(borders, 2):
    if len(borders[i] & borders[j]) == 2:
        nb[i].append(j)
        nb[j].append(i)

ans = 1
corners = []
for k, v in nb.items():
    if len(v) == 2:
        ans *= k
        corners.append(k)
print(ans)

def extend_grid(g, pos, used):
    b = calc_borders(g[pos][1])
    for i in nb[g[pos][0]]:
        if i not in used:
            for x in flip_rot(d[i]):
                bx = calc_borders(x)
                if bx[1] == b[0]:
                    g[(pos[0], pos[1] + 1)] = (i, x)
                    used.add(i)
                if bx[2] == b[3]:
                    g[(pos[0] + 1, pos[1])] = (i, x)
                    used.add(i)

for x in flip_rot(d[corners[0]]):
    g = {}
    used = set([corners[0]])
    g[(0, 0)] = (corners[0], x)
    extend_grid(g, (0, 0), used)
    if len(g.values()) == 3:
        for i in range(12):
            for j in range(12):
                extend_grid(g, (i, j), used)
        break

img = np.concatenate([np.concatenate([g[(i, 11 - j)][1][1:-1, 1:-1] for i in range(12)], axis=1) for j in range(12)], axis=0)

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
monster_all, m_hashes = [], set()
for m in flip_rot(np.array([[x for x in y] for y in monster.splitlines()])):
    if str(m) not in m_hashes:
        m_hashes.add(str(m))
        monster_all.append(m)

N, M = img.shape
ans = 0
for cur_m in monster_all:
    N_m, M_m = cur_m.shape
    for i in range(N - N_m + 1):
        for j in range(M - M_m + 1):
            test = img[i:i + N_m, j:j + M_m] == cur_m
            if all(test[k, l]  for k in range(N_m) for l in range(M_m) if cur_m[k, l] == '#'):
                ans += 1

print(''.join(np.concatenate(img)).count('#') - monster.count('#') * ans)

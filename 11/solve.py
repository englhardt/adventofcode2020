import copy

def num_neighbors(d, i, j, skip_floor=False):
    in_bounds = lambda k, l: 0 <= k < len(d) and 0 <= l < len(d[k])
    n = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            k, l = i + di, j + dj
            while skip_floor and in_bounds(k, l) and d[k][l] == '.':
                k, l = k + di, l + dj
            if in_bounds(k, l) and d[k][l] == '#':
                n += 1
    return n

def evolve(d, max_occ=4, skip_floor=False):
    d_new = copy.deepcopy(d)
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] == 'L' and num_neighbors(d, i, j, skip_floor) == 0:
                d_new[i][j] = '#'
            elif d[i][j] == '#' and num_neighbors(d, i, j, skip_floor) >= max_occ:
                d_new[i][j] = 'L'
    return d_new

def sim(d, max_occ, skip_floor):
    while True:
        d_new = evolve(d, max_occ, skip_floor)
        if all(d[i] == d_new[i] for i in range(len(d))):
            break
        d = d_new
    return sum(sum(x == '#' for x in l) for l in d)

d = [list(x) for x in open("input.txt").read().splitlines()]
print(sim(d, 4, False))
print(sim(d, 5, True))

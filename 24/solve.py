# Cube coordinates: https://www.redblobgames.com/grids/hexagons/

d = open("input.txt").read().splitlines()
g = {}
for l in d:
    i = 0
    x, y, z = (0, 0, 0)
    while i < len(l):
        if l[i:].startswith('sw'):
            x, y, z = x - 1, y, z + 1
            i += 2
        elif l[i:].startswith('se'):
            x, y, z = x, y - 1, z + 1
            i += 2
        elif l[i:].startswith('nw'):
            x, y, z = x, y + 1, z - 1
            i += 2
        elif l[i:].startswith('ne'):
            x, y, z = x + 1, y, z - 1
            i += 2
        elif l[i] == 'w':
            x, y, z = x - 1, y + 1, z
            i += 1
        elif l[i] == 'e':
            x, y, z = x + 1, y - 1, z
            i += 1
    g[(x, y, z)] = not g.get((x, y, z), False)
print(sum(g.values()))

dirs = ((-1, 0, 1), (0, -1, 1), (0, 1, -1), (1, 0, -1), (-1, 1, 0), (1, -1, 0))
for i in range(100):
    g_new = g.copy()
    pos = set(g.keys())
    for k in g:
        for dx, dy, dz in dirs:
            pos.add((k[0] + dx, k[1] + dy, k[2] + dz))
    for k in pos:
        n = 0
        for dx, dy, dz in dirs:
            n += g.get((k[0] + dx, k[1] + dy, k[2] + dz), False)
        if n == 2:
            g_new[k] = True
        elif (n == 0 or n > 2) and g.get(k, False):
            g_new[k] = False
    g = g_new
print(sum(g.values()))

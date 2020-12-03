import numpy as np

def check(d, x_c, y_c):
    x_len, y_len = len(d[1]), len(d)
    pos = [0, 0]
    ans = 0
    while pos[1] < y_len:
        ans += d[pos[1]][pos[0] % x_len]
        pos[0], pos[1] = pos[0] + x_c, pos[1] + y_c
    return ans

d = [[x == '#' for x in l] for l in open("input.txt").read().splitlines()]
print(check(d, 3, 1))
print(np.prod(list(map(lambda x: check(d, x[0], x[1]), [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]))))

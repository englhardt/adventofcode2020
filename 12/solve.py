import numpy as np

d = open("input.txt").read().splitlines()
moves = {'N': [0, 1], 'S': [0, -1], 'W': [-1, 0], 'E': [1, 0]}
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# Part 1
pos, dr = np.array([0, 0]), 0
for x in d:
    if x[0] in moves.keys():
        pos += np.array(moves[x[0]]) * int(x[1:])
    elif x[0] == 'L':
        dr = (dr - int(x[1:]) // 90) % len(dirs)
    elif x[0] == 'R':
        dr = (dr + int(x[1:]) // 90) % len(dirs)
    elif x[0] == 'F':
        pos += np.array(dirs[dr]) * int(x[1:])
print(sum(abs(pos)))

# Part 2
pos, wp = np.array([0, 0]), np.array([10, 1])
for x in d:
    if x[0] in moves.keys():
        wp += np.array(moves[x[0]]) * int(x[1:])
    elif x[0] == 'L':
        for _ in range(int(x[1:]) // 90):
            wp[0], wp[1] = -wp[1], wp[0]
    elif x[0] == 'R':
        for _ in range(int(x[1:]) // 90):
            wp[0], wp[1] = wp[1], -wp[0]
    elif x[0] == 'F':
        pos += np.array(wp) * int(x[1:])
print(sum(abs(pos)))

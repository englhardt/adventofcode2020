def score(x):
    return sum((len(x) - i) * n for i, n in enumerate(x))

def play(a, b, p2=False):
    seen = set()
    while len(a) > 0 and len(b) > 0:
        h = str(a) + str(b)
        if p2 and h in seen:
            return 1, score(a)
        seen.add(h)
        x, y = a.pop(0), b.pop(0)
        if p2 and len(a) >= x and len(b) >= y:
            winner, _ = play(a[:x], b[:y], p2)
        else:
            winner = 1 if x > y else 2
        if winner == 1:
            a += [x, y]
        else:
            b += [y, x]
    return (1, score(a)) if len(a) > 0 else (2, score(b))

d = open("input.txt").read().split('\n\n')
a = [int(x) for x in d[0][10:].split('\n')]
b = [int(x) for x in d[1][10:].rstrip().split('\n')]
print(play(a[:], b[:])[1])
print(play(a, b, True)[1])

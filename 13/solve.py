d = open("input.txt").read().splitlines()
n = int(d[0])
b = {int(t): i for i, t in enumerate(d[1].split(',')) if t != 'x'}

# Part 1
sim = {i: 0 for i in b.keys()}
while min(sim.values()) < n:
    for i in sim.keys():
        sim[i] += i if sim[i] < n else 0
print(min(sim, key=sim.get) * (min(sim.values()) - n))

# Part 2: Chinese remainder theorem
step = 1
for i, off in b.items():
    while (n + off) % i != 0:
        n += step
    step *= i
print(n)

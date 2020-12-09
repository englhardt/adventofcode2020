d = [int(x) for x in open("input.txt").read().splitlines()]
t = 0
for i in range(25, len(d)):
    found = False
    for j in range(i - 25, i):
        for k in range(i - 25, i):
            if j != k and d[j] + d[k] == d[i]:
                found = True
    if not found:
        t = d[i]
        print(t)

for i in range(len(d)):
    for j in range(i + 2, len(d)):
        if sum(d[i:j]) == t:
            print(min(d[i:j]) + max(d[i:j]))

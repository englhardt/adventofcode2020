t = str.maketrans('FBRL', '0110')
d = set([int(l.translate(t), 2) for l in open("input.txt").read().splitlines()])
print(max(d))
for i in range(max(d)):
    if i not in d and i - 1 in d and i + 1 in d:
        print(i)

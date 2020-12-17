import re
from collections import defaultdict

d = open("input.txt").read().splitlines()
rules = defaultdict(list)
i = 0
while len(d[i]) > 0:
    for x in re.findall(r'\d+-\d+', d[i]):
        a, b = [int(x) for x in x.split('-')]
        rules[d[i].split(':')[0]].append(range(a, b+1))
    i += 1
yt = [int(x) for x in d[i + 2].split(',')]
ot = [[int(x) for x in d[j].split(',')] for j in range(i + 5, len(d))]

# Part 1
valid = lambda x: any(x in sr for r in rules.values() for sr in r)
print(sum(0 if valid(x) else x for t in ot for x in t))

# Part 2
ft = [yt]
for t in ot:
    if all(valid(x) for x in t):
        ft.append(t)

valid_val = lambda x, y: any(x in r for r in rules[y])
valid_att = lambda a, i: all(valid_val(x[i], a) for x in ft)

poss_att = dict()
for a in rules.keys():
    poss_att[a] = [i for i in range(len(yt)) if valid_att(a, i)]

used, ans = set(), 1
for a in sorted(poss_att, key=lambda x: len(poss_att[x])):
    for i in [x for x in poss_att[a] if x not in used]:
        used.add(i)
        if a.startswith('departure'):
            ans *= yt[i]
print(ans)

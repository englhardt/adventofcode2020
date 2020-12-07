import re
from collections import defaultdict

contains = defaultdict(list)
containedin = defaultdict(set)
for l in open("input.txt").read().splitlines():
    c = l.split(' bags contain ')[0]
    for (n, o) in re.findall(r'(\d+) (\w+ \w+) bags?[,.]', l):
        contains[c].append((o, int(n)))
        containedin[o].add(c)

def check(c, ans):
    for o in containedin[c]:
        ans.add(o)
        check(o, ans)
ans = set()
check('shiny gold', ans)
print(len(ans))

def cost(c):
    ans = 0
    for o, n in contains[c]:
        ans += n + n * cost(o)
    return ans
print(cost('shiny gold'))

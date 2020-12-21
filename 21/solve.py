r = open("input.txt").read().splitlines()
d = []
for l in r:
    x = l.split(' (contains ')
    d.append((set(x[0].split()), set(x[1][:-1].split(', '))))

food = {}
for ings, alls in d:
    for a in alls:
        if a in food:
            food[a] &= set(ings)
        else:
            food[a] = set(ings)

matched_ings = set.union(*list(food.values()))
all_ings = set([y for x in d for y in x[0]])
unmatched_ings = all_ings - matched_ings
print(len([y for x in d for y in x[0] if y in unmatched_ings]))

matching = {}
while len(food) > 0:
    found = None
    for a, ings in food.items():
        if len(ings) == 1 and found is None:
            matching[a] = list(ings)[0]
            found = a
    del food[found]
    for a in food:
        food[a] -= set([matching[found]])
print(','.join(matching[k] for k in sorted(matching.keys())))

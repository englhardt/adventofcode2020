d = open("input.txt").read().strip().split('\n\n')
print(sum([len(set(x.replace('\n', ''))) for x in d]))
print(sum(len(set.intersection(*list(map(set, x.split('\n'))))) for x in d))

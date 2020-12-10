from collections import defaultdict

d = [int(x) for x in open("input.txt").read().splitlines()]
d = [0] + sorted(d) + [max(d) + 3]

# Part 1
diff = defaultdict(int)
for i in range(1, len(d)):
    diff[d[i] - d[i-1]] += 1
print(diff[1] * diff[3])

# Part 2 with dynamic programming
num = defaultdict(int)
num[0] = 1
for i in d[1:]:
    num[i] = num[i - 1] + num[i - 2] + num[i - 3]
print(num[d[-1]])

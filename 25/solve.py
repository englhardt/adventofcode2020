x, y = [int(x) for x in open("input.txt").read().splitlines()]
for l in range(10000000):
    if pow(7, l, 20201227) == x:
        print(pow(y, l, 20201227))
        break

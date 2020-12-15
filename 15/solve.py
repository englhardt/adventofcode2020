def run(x, n):
    x += [0]
    spoken = {x: i for i, x in enumerate(x[:-1])}
    for i in range(len(x), n):
        if x[-1] not in spoken:
            x.append(0)
        else:
            x.append(i - spoken[x[-1]] - 1)
        spoken[x[-2]] = i - 1
    return x

d = [0,14,6,20,1,4]
print(run(d, 2020)[-1])
print(run(d, 30000000)[-1])

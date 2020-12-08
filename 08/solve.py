import re

def run(d):
    i, acc = 0, 0
    done = [False for _ in range(len(d))]
    while True:
        if i >= len(d):
            return acc, True
        if done[i]:
            return acc, False
        done[i] = True
        ins, n = d[i]
        if ins == "jmp":
            i += int(n)
        elif ins == "acc":
            acc += int(n)
            i += 1
        elif ins == "nop":
            i += 1

d = open("input.txt").read().splitlines()
d = [re.findall(r'(\w+) ([+-]?\d+)', x)[0] for x in d]
print(run(d)[0])
for i in range(len(d)):
    if d[i][0] in ["jmp", "nop"]:
        x = d[:]
        x[i] = ("nop" if d[i][0] == "jmp" else "jmp", x[i][1])
        acc, noinfty = run(x)
        if noinfty:
            print(acc)

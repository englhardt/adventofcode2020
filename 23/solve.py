class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

def play(x, p2=False):
    x = [int(i) for i in x]
    if p2:
        x += [i for i in range(10, 1_000_000 + 1)]
    s = Node(x[0])
    d = {s.val: s}
    for i, v in enumerate(x[1:]):
        d[v] = Node(v)
        d[x[i]].next = d[v]
    d[x[-1]].next = d[x[0]]

    for i in range(10_000_000 if p2 else 100):
        a, b, c = s.next, s.next.next, s.next.next.next
        dest = s.val - 1 or max(x)
        while dest in [a.val, b.val, c.val]:
            dest -= 1
            if dest == 0:
                dest = max(x)
                break
        s.next = c.next
        c.next = d[dest].next
        d[dest].next = a
        s = s.next
    return d

x = "583976241"
d = play(x)
s = d[1]
ans = ""
while s.next.val != 1:
    ans += str(s.next.val)
    s = s.next
print(ans)
d = play(x, True)
print(d[1].next.val * d[1].next.next.val)

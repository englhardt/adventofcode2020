from lark import Lark, LarkError

def count(r, d, part2=False):
    if part2:
        r = r.replace('\n8: 42', '\n8: 42 | 42 8')
        r = r.replace('\n11: 42 31', '\n11: 42 31 | 42 11 31')
    r = r.translate(str.maketrans('0123456789', 'abcdefghij'))
    g = Lark(r, start='a')

    ans = 0
    for x in d.splitlines():
        try:
            ans += g.parse(x) is not None
        except LarkError:
            continue
    return ans

r, d = open("input.txt").read().split('\n\n')
print(count(r, d))
print(count(r, d, True))

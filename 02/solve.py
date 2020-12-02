def check1(s):
    l, u = map(int, s[0].split("-"))
    return l <= s[2].count(s[1][0]) <= u

def check2(s):
    l, u = map(int, s[0].split("-"))
    return (s[2][l - 1] == s[1][0]) != (s[2][u - 1] == s[1][0])

d = open("input.txt").read().splitlines()
print(sum([check1(x.split()) for x in d]))
print(sum([check2(x.split()) for x in d]))

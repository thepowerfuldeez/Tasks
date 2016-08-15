import sys

sys.setrecursionlimit(99999)

sys.stdin = open("aplusb.in")
sys.stdout = open("aplusb.out", "w")

t = input()
n = len(t)
c = int(t)
res = 0


def povt(x):
    s = str(x)
    t = s[0]
    for i in range(1, len(s)):
        if t == s[i]:
            return False
        t = s[i]
    return True


def f(c, x=10**(n-1)):
    global res
    a, b = x, c - x
    if x == c or b < 10 ** (n - 1):
        return
    if povt(a) and povt(b):
        res += 1
        f(c, x + 1)
    else:
        return f(c, x + 1)

f(c)
print(res % (10**9+7))
import sys

sys.stdin = open("round.in")
sys.stdout = open("round.out", "w")

n, m = map(int, input().split())
a = [int(x) for x in input().split()]
s = sum(a)
b = []

for elem in a:
    x = elem / s * m
    if int(x) - x == 0:
        b.append((int(x), int(x)))
    else:
        b.append((int(x), int(x) + 1))

a = [p[0] for p in b]
s = sum(a)

for i in range(len(b)):
    if s == m:
        break
    a[i] = b[i][1]
    s = s - b[i][0] + b[i][1]

print(*a)
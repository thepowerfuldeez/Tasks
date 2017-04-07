import sys

sys.stdin = open("slalom.in")
sys.stdout = open("slalom.out", "w")

n = int(input())
a = []
r = [[0] * n for i in range(n)]
for i in range(n):
    a.append([int(i) for i in input().split()])
a.append([0] * (n + 1))

r[0][0] = a[0][0]
for i in range(1, n):
    for j in range(i + 1):
        r[i][j] = max(a[i][j] + r[i - 1][j], a[i][j] + r[i - 1][j - 1])

print(max(r[-1]))








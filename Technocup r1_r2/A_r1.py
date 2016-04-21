n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(input())

a = a[::-1]
x = []

for index in range(m):
    l = 0
    for line in a:
        if line[index] == "*":
            l += 1
    x.append(l)

print(x)
try:
    mp = max([x[i+1] - x[i] for i in range(m-1) if x[i+1] - x[i] >= 0])
except:
    mp = 0
try:
    ms = max([x[i] - x[i+1] for i in range(m-1) if x[i] - x[i+1] >= 0])
except:
    ms = 0

print(mp, ms)


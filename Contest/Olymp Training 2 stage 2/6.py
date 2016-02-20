import sys

sys.stdin = open("cond.in")
sys.stdout = open("cond.out", "w")

n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
d = [[int(i) for i in input().split()] for i in range(m)]

d.sort(key=lambda x: x[1])
a.sort()

i = 0
summ = 0
while i < n:
    j = 0
    while j < m:
        if d[j][0] >= a[i]:
            summ += d[j][1]
            break
        j += 1
    i += 1

print(summ)


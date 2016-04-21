import sys
import math

#sys.stdin = open("a1.txt")

a = list(map(int, input().split()))

#1
res = 0
x = sum(a)
x -= 3000
res += 350
while x > 0:
    x -= 300
    res += 30
print(res, 0)

#2
res = 0
for day in a:
    if day == 0:
        continue
    elif 0 < day < 501:
        res += 29
    else:
        res = -1
        break
if res >= 0:
    print(res, 0)
else:
    print(res)

#3
t = sum(a) * 1.2
ax = math.trunc(t)
bx = (t - ax) * 100
print("{} {}".format(ax, math.ceil(bx)))

#4
print(790, 0)

#5
if sum(a) <= 16000:
    print(590, 0)
else:
    print(-1)
N = int(input())
a = list(map(int, input().split()))
prev = 0
toberemoved = []
k = 0

for i in a:
    if not i > prev:
        k += 1
        toberemoved.append(i)
    prev = i

print(k)
for j in toberemoved:
    print(j, end=' ')

N, M = map(int, input().split())
t = [int(i) for i in input().split()]
a = sorted(t + t, reverse=True)

x = 0
i = 0
res = []
while i < len(a):
    if x == N:
        print(i)
        print(*res)
        break
    if x > N:
        print(0)
        break

    x += a[i]
    res.append(a[i])
    i += 1

if x < N:
    print(-1)


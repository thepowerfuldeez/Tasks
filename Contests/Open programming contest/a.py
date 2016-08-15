n, k = map(int, input().split())
x = n // k

if k - n // k <= 0:
    print(0)
else:
    a = k // x
    k1 = a * (a - 1) // 2
    k2 = a * (a + 1) // 2
    print(x * ((k % x) * k2 + k1 * (x - k % x)))

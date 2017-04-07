n = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for i in range(n):
    x, y, z = map(int, input().split())
    if (z <= x or z <= y) and z % gcd(x, y) == 0:
        print("YES")
    else:
        print("NO")

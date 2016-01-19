def isPrime(a):
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    i = 3
    while i * i < a:
        if a % i == 0:
            return False
        i += 2
    return True

m, n = map(int, input().split())
switcher = 0

while m <= n:
    if isPrime(m):
        switcher += 1
        print(m)
    m += 1

if switcher == 0:
    print("Absent")
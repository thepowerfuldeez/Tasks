from itertools import product

count = 0


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


for p in product(range(1,100), range(1,100), range(1,100), repeat=1):
    x, y, z = p[0], p[1], p[2]
    try:
        if 4.9999999 <= (1 / x + 1 / y + 1 / z + 1 / gcd(x, y) + 1 / gcd(x, z) + 1 / gcd(y, z) + 1 / lcm(x,
                                                                                                    lcm(y, z))) <= 5.00000001:
            print(x, y, z)
            count += 1

    except Exception:
        pass

print(count)

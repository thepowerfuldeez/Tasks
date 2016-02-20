def gcd(a, b):
    """Python-style НОД"""

    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Math-style НОК"""

    return a * b / gcd(a, b)
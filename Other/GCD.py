def gcd(a,b):
    """Наименьший общий делитель"""
    while a != 0:
        a, b = a % b, a
    return b
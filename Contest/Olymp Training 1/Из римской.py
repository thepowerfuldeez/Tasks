def decequal(a):
    if a == "I":
        return 1
    elif a == "V":
        return 5
    elif a == "X":
        return 10
    elif a == "L":
        return 50
    elif a == "C":
        return 100
    elif a == "D":
        return 500
    elif a == "M":
        return 1000


def intodecimal(a):
    a = [decequal(i) for i in list(a)]
    res = a[0]

    for i in range(1, len(a)):
        res += a[i]
        if a[i - 1] < a[i]: res -= 2 * a[i - 1]

    return res


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(intodecimal(fin.read().strip()), file=fout)

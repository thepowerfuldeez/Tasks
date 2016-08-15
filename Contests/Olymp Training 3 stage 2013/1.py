with open("casting.in") as fin, open("casting.out", "w") as fout:
    switcher = int(fin.readline())
    n, a, b, c = map(int, fin.readline().split())

    if switcher == 2:
        print(min(a, b, c), file=fout)
    elif switcher == 1:
        x = [a, b, c]
        x.sort()
        res = x[0] - x[2] + x[1]
        if res > 0:
            print(res, file=fout)
        else:
            print(0, file=fout)

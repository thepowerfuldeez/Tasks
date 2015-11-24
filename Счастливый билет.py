def digitalroot(x):
    x = sum(int(i) for i in x)
    while x > 9:
        x = digitalroot(str(x))
    return x


with open('input.txt') as fin:
    N = fin.read()
    res = 0
    for i in range(1, len(N)):
        if digitalroot(N[:i]) == digitalroot(N[i:]):
            res = N[:i]
            break
    with open('output.txt', 'w') as fout:
        if res == 0:
            print(0, file=fout)
        else:
            print(1, file=fout)
            print(res, file=fout)

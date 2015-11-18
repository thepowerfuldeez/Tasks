def resheto(n):
    a = [i for i in range(n+1)]
    a[1] = 0

    m = 2
    while m <= n:
        if not a[m]%2: a[m] = 0
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1

    return [str(a[i]) for i in a if a[i] != 0]


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(" ".join(resheto(int(fin.read().strip()))), file=fout)
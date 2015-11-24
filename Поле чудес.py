def prefix_func(s, N):
    length = N
    p = [0 for i in range(length)]
    p[0] = 0

    k = 0
    for i in range(1, length):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

with open('input.txt') as fin:
    N = int(fin.readline())
    a = ''.join(fin.readline().split())

    with open('output.txt', 'w') as fout:
        print(max(prefix_func(a, N)), file=fout)

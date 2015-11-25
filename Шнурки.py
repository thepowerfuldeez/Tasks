with open('input.txt') as fin:
    a, b, l, N = [int(i) for i in fin.read().split()]
    with open('output.txt', 'w') as fout:
        print(2 * (l + (a + b) * (N - 1)) + a, file=fout)
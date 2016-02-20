with open("input.txt") as fin:
    n, m = map(int, fin.readline().split())
    res = set(map(int, fin.readline().split()))
    for p in fin:
        res &= set(map(int, p.split()))

    with open("output.txt", "w") as fout:
        print(len(res) + 1, file=fout)

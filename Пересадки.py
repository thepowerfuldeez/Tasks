def conjunction(a1, b1, a2, b2):
    if a1 < b1:
        set1 = set(range(a1, b1 + 1))
    else:
        set1 = set(range(b1, a1 + 1))

    if a2 < b2:
        set2 = set(range(a2, b2 + 1))
    else:
        set2 = set(range(b2, a2 + 1))

    return len(set1 & set2)

with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(conjunction(*[int(i) for i in fin.read().split()]), file=fout)
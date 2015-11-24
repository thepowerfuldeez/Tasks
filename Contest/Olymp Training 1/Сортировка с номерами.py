with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        a = fin.read().split("\n")
        for i in range(len(a)):
            a[i] = a[i].split(". ")[1]
        a.sort()

        for index, value in enumerate(a):
            print("%d. %s" % (index + 1, value), file=fout)

with open("input.txt") as fin:
    n, d = map(int, fin.readline().split())
    c = [int(i) for i in fin.readline().split()]

count = 0

c.sort()
i = 0

while i < len(c) - 1:
    if abs(c[i] - c[i + 1]) <= d:
        del c[i]
        del c[i]
        count += 1
    else:
        i += 1

with open("output.txt", "w") as fout:
    print(count, file=fout)

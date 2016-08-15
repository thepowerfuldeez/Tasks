with open("input.txt") as fin:
    n = int(fin.readline())
    e = map(int, fin.readline().split())
    c = [int(i) for i in fin.readline().split()]
    p = map(int, fin.readline().split())

etime = []
ptime = []
temp = 0
for t in e:
    temp += t
    etime.append(temp)
temp = 0
for t in p:
    temp += t
    ptime.append(temp)

j = 0
res = 0
for i in range(n - 1):
    if etime[i] - ptime[i] > j and etime[i + 1] - ptime[i + 1] >= j:
        j += 1
        res += c[i]
if etime[n - 1] - ptime[n - 1] > j:
    res += c[n - 1]

with open("output.txt", "w") as fout:
    print(res, file=fout)

with open('input.txt') as fin:
    N = int(fin.readline())
    a = [int(i) for i in fin.read().strip().split()]

a.sort()
res = 0
# temp = 0
# for i in range(len(a)):
#    if a[i] + temp < 4:
#        temp += a[i]
#    else:
#        temp = min(temp, a[i])
#        res += 1
#
# if temp > 0:
#    res += 1

heh = range(len(a))
for i in heh:
    for j in (list(heh)[0:i]+list(heh)[i:]):
        if a[i] + a[j] == 4 and a[0] != 2:
            res += 1
            a[j], a[i] = 0, 0


with open('output.txt', 'w') as fout:
    print(res, file=fout)

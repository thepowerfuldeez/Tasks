with open('input.txt') as fin:
    a = list(fin.read())
n = 0
if 1072 <= ord(a[0]) <= 1103:
    n += 1
for i in range(1, len(a) - 1):
    if abs(ord(a[i]) - ord(a[i + 1])) > 102:
        n += 1

with open('output.txt', 'w') as fout:
    print((n + 1) * len(a), file = fout)

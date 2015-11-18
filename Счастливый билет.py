def digitalroot(x):
    x = sum([int(i) for i in x])
    while x > 9:
        x = digitalroot(str(x))
    return x

fin = open('input.txt')
N = fin.read()
fin.close()
res = 0

for i in range(len(N)):
    if digitalroot(N[:i]) == digitalroot(N[i:]):
        res = N[:i]
        break

fout = open('output.txt', 'w')
if res == 0:
    print(0, file = fout)
else:
    print(1, file = fout)
    print(res, file = fout)
fout.close()
from itertools import combinations as cmb

with open("trap.in") as fin:
    n, x, y = map(int, fin.readline().split())
    a = map(int, fin.readline().split())

fout = open("trap.out", "w")

switcher = False

for c in cmb(a, r=2):
    if not c[0] + c[1] > x and not abs(c[0] - c[1]) < y:
        switcher = True
        print(*c, file=fout)

if not switcher:
    print(0, file=fout)

fout.close()

import sys

fin = open("input.txt")
n = int(fin.readline())
a = int(fin.readline())
b = int(fin.readline())
c = int(fin.readline())
d = int(fin.readline())
fin.close()
fout = open("output.txt", "w")

if not a + c <= n <= b + d:
    print(0, file=fout)
    fout.close()
    sys.exit(0)

if c - 1 < n - a < d + 1:
    res = min(abs(n - a - c), b - a) + 1
    print(res, file=fout)
    fout.close()
    sys.exit(0)
else:
    if c - 1 < n - b < d + 1:
        res = min(b - a, b + d - n) + 1
        print(res, file=fout)
        fout.close()
        sys.exit(0)
    if a - 1 < n - d < b + 1:
        res = min(d - c, b + d - n) + 1
        print(res, file=fout)
        fout.close()
        sys.exit(0)

print(0, file=fout)
fout.close()
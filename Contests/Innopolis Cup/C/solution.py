# from itertools import product
#
# with open("xor.in") as fin:
#     n = int(fin.readline())
#     a = list(map(int, fin.readline().split()))
#     s = int(fin.readline())
#
# fout = open("xor.out", "w")
# switcher = False
#
# def xoring(a):
#     res = a[0]
#     if len(a) > 1:
#         for x in a[1:]:
#             res ^= x
#     return res
#
# for elem in product(range(6), repeat=n):
#     for i in range(n):
#         if not list(elem)[i] <= a[i]:
#             continue
#
#     res = xoring(elem)
#     if res == s:
#         switcher = True
#         print("YES", file=fout)
#         for x in elem:
#             print(x, file=fout, end=" ")
#         break
#
# if not switcher:
#     print("NO", file=fout)
#
# fout.close()



with open("xor.in") as fin:
    n = int(fin.readline())
    a = map(int, fin.readline().split())
    s = int(fin.readline())

fout = open("xor.out", "w")

switcher = False
t = []
text = ""
RES = [""] * n


def xoring(a):
    if not a == []:
        res = int(a[0])
        if len(a) > 1:
            for x in a[1:]:
                res ^= int(x)
        return str(res)


a = sorted(a, reverse=True)
for i in range(len(a)):
    a[i] = str(bin(a[i]))[2:]
for i in range(len(a[0])):

    xor = xoring(t)
    if not xor is None:
        text += xor

    t = []

    for num in a:
        if i > len(num) - 1:
            continue
        num = num[::-1]
        t.append(num[i])

res_xor = int(("{:d}".format(int(text[::-1]))), 2)

s_xor = str(bin(s))[2:]
for i in range(len(s_xor)):
    if n % 2 == 0:
        if s_xor[i] == "1":
            x1 = 0
            while x1 < n / 2:
                RES[x1] += "1"
                x1 += 1
                RES[x1] += "0"
                x1 += 1
        if s_xor[i] == "0":
            x2 = 0
            while x2 < n:
                RES[x2] += "1"
                x2 += 1
    else:
        if s_xor[i] == "1":
            x3 = 0
            while x3 < n:
                RES[x3] += "1"
                x3 += 1
        if s_xor[i] == "0":
            RES[0] += "1"
            x4 = 1
            while x4 < (n - 1) / 2:
                RES[x4] += "0"
                x4 += 1
                RES[x4] += "1"
                x4 += 1

if RES is not [""]*n:
    switcher = True
    print("YES", file=fout)
    for tex in RES:
        if tex == '':
            continue
        print(int(tex, 2), file=fout, end=' ')

if not switcher:
    print("NO", file=fout)

fout.close()

from itertools import product
import sys

def is_palyndrome(a):
    return a[:len(a) // 2] == a[::-1][:-len(a) // 2]

s8 = ["".join(i) for i in product("ab",repeat=8) if is_palyndrome(i)]
s7 = ["".join(i) for i in product("ab",repeat=7) if is_palyndrome(i)]
s6 = ["".join(i) for i in product("ab",repeat=6) if is_palyndrome(i)]
s5 = ["".join(i) for i in product("ab",repeat=5) if is_palyndrome(i)]
s4 = ["".join(i) for i in product("ab",repeat=4) if is_palyndrome(i)]
s3 = ["".join(i) for i in product("ab",repeat=3) if is_palyndrome(i)]
s2 = ["".join(i) for i in product("ab",repeat=2) if is_palyndrome(i)]

s = input()
l = len(s)

if is_palyndrome(s):
    print(0)
    print(s)
    sys.exit(0)

if l == 1:
    print(1)
    print(s)
    sys.exit(0)
elif l == 2:
    res = [s3[i] for i in range(len(s3)) if s in s3[i]]
    if res:
        print(1)
        print(res[0])
        sys.exit(0)
    res = [s4[i] for i in range(len(s4)) if s in s4[i]]
    if res:
        print(2)
        print(res[0])
        sys.exit(0)
elif l == 3:
    res = [s4[i] for i in range(len(s4)) if s in s4[i]]
    if res:
        print(1)
        print(res[0])
        sys.exit(0)
    res = [s5[i] for i in range(len(s5)) if s in s5[i]]
    if res:
        print(2)
        print(res[0])
        sys.exit(0)
    res = [s6[i] for i in range(len(s6)) if s in s6[i]]
    if res:
        print(3)
        print(res[0])
elif l == 4:
    res = [s5[i] for i in range(len(s5)) if s in s5[i]]
    if res:
        print(1)
        print(res[0])
        sys.exit(0)
    res = [s6[i] for i in range(len(s6)) if s in s6[i]]
    if res:
        print(2)
        print(res[0])
        sys.exit(0)
    res = [s7[i] for i in range(len(s7)) if s in s7[i]]
    if res:
        print(3)
        print(res[0])
        sys.exit(0)
    res = [s8[i] for i in range(len(s8)) if s in s8[i]]
    if res:
        print(4)
        print(res[0])
        sys.exit(0)



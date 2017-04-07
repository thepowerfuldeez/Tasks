import sys

sys.stdin = open("smallnim.in")
sys.stdout = open("smallnim.out", "w")

input()
a = [int(i) for i in input().split()]
x = [b for b in a if b == min(a)]
try:
    if len(x) % 2 == 0 or len(x) == 1:
        if x[0] > 1:
            print("YES")
            print(x[0] - 1)
        elif x[0] == 1:
            print("YES")
            print(1)
        else:
            print("NO")
    else:
        print("NO")
except:
    print("NO")
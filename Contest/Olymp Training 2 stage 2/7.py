import sys
import itertools

sys.stdin = open("sweets.in")
#sys.stdout = open("sweets.out", "w")

N, a, b, c = map(int, input().split())

temp = 0

for A in range(1, N):
    for B in range(1, N):
        C = N - A - B
        for p in itertools.permutations([a, b, c]):
            res = A // p[0] * B // p[1] * C // p[2]
            if res > temp:
                temp = res
                otv = [A, B, C]


print(" ".join(str(i) for i in otv))
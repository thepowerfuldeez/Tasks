import sys
import itertools


def dice():
    for i in range(1, 7):
        yield i

sys.stdout = open("dice.out", "w")
sys.stdin = open("dice.in")

m, n = map(int, input().split())
res = 0
for p in itertools.product(dice(), repeat=m):
    if int("".join([str(i) for i in p])) % n == 0:
        res += 1
print("{:.3f}".format(res / 6 ** m))
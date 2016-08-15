import sys

sys.stdin = open("bb8.in")
sys.stdout = open("bb8.out", "w")

a, b, h, w = map(int, input().split())

if w % b == 0:
    res = w // b
else:
    res = w // b + 1

if h % a == 0:
    res *= h // a
else:
    res *= (h // a + 1)

print(res)
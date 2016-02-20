import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")

n = input()
v = sorted(input().split(), reverse=True)
p = sorted(input().split())

k = 0
for i in range(int(n)):
    if v[i] >= p[i]:
        k += 1
print(k)
print(" ".join(v))
print(" ".join(p))

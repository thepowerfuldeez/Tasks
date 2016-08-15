import sys

def definition2(x):
    if x == "L":
        return -1
    elif x == "R":
        return 1


sys.stdin = open("droids.in")
sys.stdout = open("droids.out", "w")

n, m = map(int, input().split())
s = input()
algo = input()

droids = []
rocks = set()

for i in range(len(s)):
    if s[i] == "D":
        droids.append(i)
    elif s[i] == "#":
        rocks.add(i)
alg = [definition2(x) for x in algo]

for i in range(len(droids)):
    delta = 0
    for d in alg:
        delta += d
        if droids[i] + delta in rocks or droids[i] + delta >= n or droids[i] + delta < 0:
            droids[i] = 0
            break

temp = [droids[i] for i in range(len(droids)) if droids[i] != 0]
print(len(temp))
print(" ".join([str(i + 1) for i in temp]))
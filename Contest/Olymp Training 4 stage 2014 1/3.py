import sys

sys.stdin = open("olympiad.in")
sys.stdout = open("olympiad.out", "w")


n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
b = sorted(a, key=lambda x: x[2], reverse=True)

c = 0
i = 0
tasks_m = [0]*n
tasks = []
t_all = 0
while i < n:
    t = b[i][1]
    if t_all > t:
        break
    for j in range(i+1, n):
        if not tasks_m[j]:
            if b[j][0] + b[j][1] <= t:
                c += b[j][2]
                tasks.append(str(a.index(b[j]) + 1))
                tasks_m[j] = 1
                break
    t_all += t + b[i][0]
    c += b[i][2]
    tasks.append(str(a.index(b[i]) + 1))
    i += 1

print(c)
print(len(tasks))
print(" ".join(tasks))
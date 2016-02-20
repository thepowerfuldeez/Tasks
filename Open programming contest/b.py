from sys import exit


def in_segment(j, x):
    for i in range(n):
        if x[i][0] <= j <= x[i][1]:
            return True
    return False


fin = open("input.txt")
n, a, b, c = map(int, fin.readline().split())

fout = open("output.txt", "w")
x = []
sum = 0

for i in range(n):
    l, r = map(int, fin.readline().split())
    x.append([l, r])
    time = r - l + 1
    sum += time
fin.close()

x.sort()

if sum > a:
    print("No", file=fout)
    fout.close()
    exit(0)

for trip in x:
    new_sum = 0
    for j in range(trip[0], trip[0] + b):
        if in_segment(j, x):
            new_sum += 1
    if new_sum > c:
        print("No", file=fout)
        fout.close()
        exit(0)

print("Yes", file=fout)
fout.close()

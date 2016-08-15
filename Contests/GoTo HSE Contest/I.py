import sys


def voln(x, y, cur, n, m, A):
    A[x][y] = cur
    if y + 1 < m:
        if A[x][y + 1] == 0 or (A[x][y + 1] != -1 and A[x][y + 1] > cur):
            voln(x, y + 1, cur + 1, n, m, A)
    if x + 1 < n:
        if A[x + 1][y] == 0 or (A[x + 1][y] != -1 and A[x + 1][y] > cur):
            voln(x + 1, y, cur + 1, n, m, A)
    if x - 1 >= 0:
        if A[x - 1][y] == 0 or (A[x - 1][y] != -1 and A[x - 1][y] > cur):
            voln(x - 1, y, cur + 1, n, m, A)
    if y - 1 >= 0:
        if A[x][y - 1] == 0 or (A[x][y - 1] != -1 and A[x][y - 1] > cur):
            voln(x, y - 1, cur + 1, n, m, A)
    if y + 1 < m and x + 1 < m:
        if A[x + 1][y + 1] == 0 or (A[x + 1][y + 1] != -1 and A[x + 1][y + 1] > cur):
            voln(x + 1, y + 1, cur + 1, n, m, A)
    if x - 1 < n and y - 1 < n:
        if A[x - 1][y - 1] == 0 or (A[x - 1][y - 1] != -1 and A[x - 1][y - 1] > cur):
            voln(x - 1, y - 1, cur + 1, n, m, A)
    if x - 1 >= 0 and y + 1 >= 0:
        if A[x - 1][y + 1] == 0 or (A[x - 1][y + 1] != -1 and A[x - 1][y + 1] > cur):
            voln(x - 1, y + 1, cur + 1, n, m, A)
    if y - 1 >= 0 and x + 1 >= 0:
        if A[x + 1][y - 1] == 0 or (A[x + 1][y - 1] != -1 and A[x + 1][y - 1] > cur):
            voln(x + 1, y - 1, cur + 1, n, m, A)
    return A

sys.stdin = open("input.txt")

H, W = map(int, input().split())
A = []
for i in range(H):
    t = input().replace(".", "0").replace("X", "1")
    A.append([int(i) for i in list(t)])
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
A = A[::-1]

S = voln(sx - 1, sy - 1, 1, H, W, A)
print(S)



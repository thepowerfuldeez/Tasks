fin = open('input.txt', 'r')
N = int(fin.readline())
a = [list(map(int, line.strip().split())) for line in fin]
fin.close()


def delete_island(x, y):
    a[x][y] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        if 0 <= x1 < N and 0 <= y1 < N:
            if a[x1][y1] == 1:
                delete_island(x1, y1)


count = 0

for j in range(N):
    for i in range(N):
        if a[i][j] == 1:
            delete_island(i, j)
            count += 1

open('output.txt', 'w').write(str(count))

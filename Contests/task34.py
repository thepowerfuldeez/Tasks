f = open('input.txt')
N = int(f.readline())
a = []
for line in f:
    a.append([int(i) for i in line.split()])

i = N-1
j = 0
summ = a[i][j]
while True:
    if j == N-1 and i >= 0:
        while i >= 1:
            summ += a[i-1][j]
            i -= 1
        break
    if j < N-1 and i == 0:
        while j < N-1:
            summ += a[i][j+1]
            j += 1
        break

    if a[i-1][j] > a[i][j+1]:
        summ += a[i-1][j]
        i -= 1
    if a[i][j+1] > a[i-1][j]:
        summ += a[i][j+1]
        j += 1

f = open('output.txt', 'w')
f.write(str(summ))

f.close()  
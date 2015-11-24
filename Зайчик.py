"""Зайчику в клетке поставили лесенку. Лестница имеет определенное
количество ступенек N. Заяц может одним прыжком преодолеть не более К
ступенек. Для разнообразия зайчик пытается каждый раз найти новый путь к
вершине лестницы. Сколько различных способов есть у зайца добраться до
вершины лестницы при заданных значениях K и N."""

with open('input.txt') as fin:
    N, K = [int(i) for i in fin.read().strip().split()]
    a = [1] * (N + 1)

    for i in range(1, N + 1):
        a[i] = 0
        for j in range(max(0, i - K), i):
            a[i] += a[j]

    with open('output.txt', 'w') as fout:
        print(a[N], file=fout)

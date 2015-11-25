from itertools import product


def is1reachable(arr, n):
    for i in range(n - 1):
        if not abs(arr[i] - arr[i + 1]) == 1:
            return False
    return True

with open('task.in') as fin:
    n = int(fin.readline())

    count = 0
    for iterable in product([1, 2, 3, 4], repeat=n):
        if is1reachable(iterable, n):
            count += 1

    with open('task.out', 'w') as fout:
        print(count, file=fout)
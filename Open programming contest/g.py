import sys, functools, collections

sys.setrecursionlimit(999999999)


@functools.lru_cache(2048)
def fibdeque(n):
    while n != 0:
        return 2
    res.append(step)

    return (step + 1) * fibdeque(n - 1, step) - step


with open("input.txt") as fin:
    n = int(fin.read())
fout = open("output.txt", "w")
res = collections.deque()
x = 0
step = 1


def main():
    global step
    global res
    global x

    k = 0
    temp = fibdeque(k, step)

    while temp != n:
        if temp > n:
            break
        k += 1
        res.append(step)
        temp = fibdeque(k, step)

    step = res[x]

    if temp == n:
        print(k, file=fout)
        print(" ".join([str(res[i]) for i in range(k)]), file=fout)
    else:
        res = collections.deque(res)
        res[x] = step + 1
        x += 1
        main()


main()

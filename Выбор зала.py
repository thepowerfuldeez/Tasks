from math import ceil, floor


def is_Zal(A, B, C, D):
    count = 0
    # set1 = set()
    # for i in range(A, B + 1):
    #     for j1 in range(1, A + 1):
    #         if A <= i * j1 <= B and C <= 2 * i + 2 * j1 <= D:
    #             set1.add((j1, i))
    #     for j2 in range(1, B + 1):
    #         if A <= i * j2 <= B and C <= 2 * i + 2 * j2 <= D:
    #             set1.add((j2, i))

    for i in range(1, D // 2):
        if i * i > B:
            break
        miny = max(i, ceil(C / 2 - i), ceil(A / i))
        maxy = min(floor(B / i), floor(D / 2 - i))

        count += max(0, maxy - miny + 1)

    return count


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(is_Zal(*[int(i) for i in fin.read().split()]), file=fout)

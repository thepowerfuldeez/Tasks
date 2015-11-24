def area(x1, y1, x2, y2, x3, y3):
    # x1 y1
    # x2 y2

    a1 = x3 - x1
    b1 = y3 - y1
    a2 = x2 - x1
    b2 = y2 - y1

    return abs((a1 * b2 - a2 * b1)) / 2


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        res = area(*[int(i) for i in fin.read().split()])
        if res + 0.0000000001 >= round(res, 10):
            res = round(res, 10)
        if str(res).split(".")[1] == "0":
            res = str(res).split(".")[0]
        print(res, file=fout)

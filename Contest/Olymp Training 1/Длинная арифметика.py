def BigSum(a, b):
    a = str(a)[::-1]
    b = str(b)[::-1]
    c = []
    if len(a) > len(b):
        for i in a:
            c.append(i)
        for j in range(len(b)):
            c[j] += b[j]
    elif len(a) <= len(b):
        for i in b:
            c.append(i)
        for j in range(len(a)):
            c[j] += a[j]

    summ = ''
    temp = 0
    for i in c:
        z = [int(z) for z in list(i)]
        temp_sum = sum(z)
        summ += str((temp_sum + temp) % 10)
        temp = (temp_sum + temp) // 10
    if temp != 0:
        summ += str(temp)

    return summ[::-1]


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(BigSum(*[int(i) for i in fin.read().strip().split("\n")]), file=fout)

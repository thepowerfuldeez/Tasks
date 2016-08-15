from itertools import combinations_with_replacement as cwr

with open('sensor.in') as fin:
    N = int(fin.read())
k = set()


for i in range(1, N + 1):
    for j in cwr([1, 2, 3, 4, 5, 6], r=i):
        if sum(j) == N:
            print(j)
            new_sum = sum([7 - i for i in j])
            print(new_sum)
            k.add(new_sum)

with open('sensor.out', 'w') as fout:
    print(len(k), file=fout)

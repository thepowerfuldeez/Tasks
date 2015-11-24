from math import sqrt

n = int(input("n = "))
a = list(range(n + 1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    i += 1
print(lst)


def prime(a):
    if a % 2 == 0: return False
    for i in range(3, int(sqrt(a))+1, 2):
        if a % i == 0: return False
    return True

from math import sqrt


def get_distance(a, b):
    return sqrt(abs(a - b) ** 2 + W ** 2)


with open("birch.in") as fin, open("birch.out", "w") as fout:
    L, W = map(int, fin.readline().split())
    N = int(fin.readline())
    a = [int(i) for i in fin.readline().split()]
    M = int(fin.readline())
    b = [int(i) for i in fin.readline().split()]


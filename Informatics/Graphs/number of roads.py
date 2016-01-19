num_verticles = int(input())
a = [[int(i) for i in input().split()] for j in range(num_verticles)]
b = []
for i in a:
    for j in i:
        b.append(j)
print(b.count(1) // 2)

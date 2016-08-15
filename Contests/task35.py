def count(a):
    num_ = 0
    max_ = 0
    for i in range(len(a)):
        if a[i] == 0:
            num_ += 1
        else:
            max_ = max(num_, max_)
            num_ = 0
    return max(max_, num_)

f = open('input.txt')
a = []
for line in f:
    a.append([int(i) for i in line.strip().split()])

b = []
for i in range(10):
    b.append(count(a[i]))
    b.append(count([a[j][i] for j in range(10)]))

f = open('output.txt', 'w')
f.write(str(max(b)))

f.close()

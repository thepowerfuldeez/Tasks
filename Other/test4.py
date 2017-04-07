x = input()
res = set()
a = []

for i in range(len(x)):
    for j in range(len(x), -1, -1):
        a.append(x.count(x[i:]))
        a.append(x.count(x[i:j]))
        a.append(x.count(x[j:]))
print(sorted(a))

s = 'avavrewwevavavewrewrew'
f = 'vav'


def fun(s, f):
    ind = 1
    count = 0
    while ind != -1:
        ind = s.find(f)
        if ind >= 0:
            count += 1
        s = s[ind + 1:]
    print(count)

print(fun(s, f))
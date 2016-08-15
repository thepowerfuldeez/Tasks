import datetime
import sys


def valid(x, dates, tses):
    for i in range(len(dates)):
        t = x + datetime.timedelta(days=tses[i])
        if not t >= dates[i]:
            return False
    return True


N = int(input())
a = []
for i in range(N):
    input()
    date = datetime.datetime.strptime(input(), '%d.%m.%Y')
    date -= datetime.timedelta(days=1)
    t = int(input())
    a.append([date, t])

t = list(zip(*a))
x = min(t[0])
y = max(t[1])

x -= datetime.timedelta(days=y)
res = x

z = 0
while not valid(res, t[0], t[1]):
    if z == 1000:
        print("Impossible")
        sys.exit()
    res += datetime.timedelta(days=1)
    z += 1
print("{:02d}.{:02d}.{}".format(res.day, res.month, res.year))
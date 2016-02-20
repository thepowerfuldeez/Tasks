import sys
import re

sys.stdin = open("schools.in")
sys.stdout = open("schools.out", "w")

n = int(input())
d = re.compile("\d+")
a = d.findall(" ".join(input() for i in range(n)))
res = set(filter(lambda x: a.count(x) <= 5, a))

print(len(res))
for i in res:
    print(i)

import sys

sys.stdin = open("queries.in")
sys.stdout = open("queries.out", "w")

flatten = lambda *n: (e for a in n
    for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

def generate_numbers(s):
    if s.count("?") == 0:
        yield int(s)
    t = s.partition("?")
    for i in range(10):
        x = t[0] + str(i) + t[2]
        yield generate_numbers(x)


n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [input() for i in range(m)]

# for z in b:
#     g = generate_numbers(z)
#     res = 0
#     for i in g:
#         res += len(list(filter(lambda x: x >= next(i), a)))
#     print(res)

for j in flatten(generate_numbers("?1?")):
    print(j)

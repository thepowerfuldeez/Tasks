import sys
sys.stdin = open("input.txt")
sys.stdout = open("output.txt", "w")

n, m, a, b = map(int, input().split())
t = [input() for _ in range(n)]
plites = [[int(i) for i in s.replace(".", "1").replace("*", "0")] for s in t]


def calc_cost(line):
    count = 0
    cost = 0
    last_num = None
    if line[0] == 0:
        count += 1
    for num in line:
        if num == 0:
            count += 1
            if num != last_num:
                cost += min((count // 2) * a + (count % 2) * b, count * b)
                last_num = num
                count = 0
        else:
            last_num = num
            count = 0
    cost += min((count // 2) * a + (count % 2) * b, count * b)
    return cost


cost = sum(map(calc_cost, plites))
# print(plites)
print(cost)
import sys

sys.stdin = open("cows.in")
sys.stdout = open("cows.out", "w")

m, n = map(int, input().split())
cow_coords = []
last_res = float("+inf")
for i in range(n):
    for j, x in enumerate(input()):
        if x == "C": cow_coords.append((j, i))

for selected_cow_coord in cow_coords:
    res = 0
    for cow_coord in cow_coords:
        if cow_coord != selected_cow_coord:
            res += ((cow_coord[0] - selected_cow_coord[0])**2 + (cow_coord[1] - selected_cow_coord[1])**2)
    last_res = min(res, last_res)

print(last_res)

sys.stdin.close()
sys.stdout.close()
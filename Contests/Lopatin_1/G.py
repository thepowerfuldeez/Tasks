import sys

sys.stdin = open("testsys.in")
sys.stdout = open("testsys.out", "w")

H, M, L, T, C, S = map(int, input().split())
contest_start_time = H * 60 + M
tasks = [[{"time": 0, "solved": False} for j in range(C)] for i in range(T)]
for i in range(S):
    z = input().split()
    h, m, t, c, code = int(z[0]), int(z[1]), int(z[2]), int(z[3]), z[4]

    if not tasks[t - 1][c - 1]["solved"]:
        if code == "OK":
            tasks[t - 1][c - 1]["solved"] = True
            contest_submit_time = h * 60 + m
            if contest_submit_time < contest_start_time:
                contest_submit_time += 24 * 60
            tasks[t - 1][c - 1]["time"] += contest_submit_time - contest_start_time
            continue
        else:
            tasks[t - 1][c - 1]["time"] += 20

for p in [[sum(1 for a in tasks[i] if a["solved"]), sum(a["time"] for a in tasks[i] if a["solved"])] for i in range(T)]:
    print(*p)
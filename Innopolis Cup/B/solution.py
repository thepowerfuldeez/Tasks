# for (int b1 = 1; b1 <= n; b1++) {
#             double min = 1.0;
#             for (int i = 1; i <= b1; i++) {
#                 double v = fabs((1.0 * a / b) - (1.0 * i / b1));
#                 min = fmin(min, v);
#             }
#
#             System.out.println(min);
#         }


with open("approximate.in") as fin:
    a, b, n = map(int, fin.read().split())

res = []

for b1 in range(1, n + 1):
    t = []
    for i in range(1, b1 + 1):
        t.append(abs(1.0 * a / b - 1.0 * i / b1))
    res.append(float("%.4f" % (abs(min(t) - 1.0 * a / b))))

print(list(set(res)))



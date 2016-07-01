import sys

K, M = map(int, input().split())
t = [int(i) for i in input().split()]
A = sorted(t + t, reverse=True)


F = [0] * (K + 1)
F[0] = 1
for i in range(len(A)):
    for k in range(K, A[i] - 1, -1):
        if F[k - A[i]] == 1:
            F[k] = 1
F = [0] * (K + 1)
F[0] = 1
Prev = [0] * (K + 1)
for i in range(len(A)):
    for k in range(K, A[i] - 1, -1):
        if F[k - A[i]] == 1:
            F[k] = 1
            Prev[k] = A[i]
Ans = []
k = K
while k > 0:
    Ans.append(Prev[k])
    k -= Prev[k]
# Ans = []
# k = K
# z = 0
# while k != 0:
#     if z == 10:
#         print(0)
#         sys.exit()
#     for i in range(len(A)):
#         if k - A[i] >= 0 and F[k] == F[k - A[i]] + 1:
#             Ans.append(A[i])
#             k -= A[i]
#     z += 1

for n in Ans:
    if n not in A:
        print(-1)
        sys.exit()
    A.remove(n)

print(len(Ans))
print(*Ans)
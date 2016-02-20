from itertools import combinations, product

def solution(n, k):
    x = n // k

    a = list(range(1, n + 1))
    b = [a[i:i + k] for i in range(0, n, k)]
    c = [a[i:n:x] for i in range(x)]

    count = 0

    for p in product(b, c):
        for l in product(combinations(p[0], 2), combinations(p[1], 2)):
            if len(set(l[0]) & set(l[1])) == 2:
                count += 1

    return count


print(solution(80, 20))  # 4 * 40

print(solution(16, 8))  # 2 * 12
print(solution(24, 8))  # 3 * 7
print(solution(32, 8))  # 4 * 4
print(solution(40, 8))  # 5 * 3
print(solution(48, 8))  # 6 * 2
print(solution(56, 8))  # 7 * 1
print(solution(64, 8))  # 8 * 0

print(solution(14, 7))  # 2 * 9
print(solution(21, 7))  # 3 * 5
print(solution(28, 7))  # 4 * 3
print(solution(35, 7))  # 5 * 2
print(solution(42, 7))  # 6 * 1
print(solution(49, 7))  # 7 * 0

print(solution(12, 6))  # 2 * 6
print(solution(18, 6))  # 3 * 3
print(solution(24, 6))  # 4 * 2
print(solution(30, 6))  # 5 * 1
print(solution(36, 6))  # 6 * 0
print(solution(42, 6))  # 7 * 0

print(solution(10, 5))  # 2 * 4
print(solution(15, 5))  # 3 * 2
print(solution(20, 5))  # 4 * 1
print(solution(25, 5))  # 5 * 0
print(solution(30, 5))  # 6 * 0
print(solution(35, 5))  # 7 * 0

print(solution(8, 4))  # 2 * 2
print(solution(12, 4))  # 3 * 1
print(solution(16, 4))  # 4 * 0
print(solution(20, 4))  # 5 * 0
print(solution(24, 4))  # 6 * 0
print(solution(28, 4))  # 7 * 0

print(solution(6, 3))  # 2 * 1
print(solution(9, 3))  # 3 * 0

print(solution(4, 2))  # 2 * 0

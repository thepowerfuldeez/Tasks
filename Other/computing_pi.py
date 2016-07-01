import time

cur = time.time()
n = 10**7

pi = 4 * sum((-1)**i / (2 * i + 1) for i in range(n))
print(pi)
print(time.time() - cur)
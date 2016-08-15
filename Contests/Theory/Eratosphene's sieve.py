import time


def sieve(n):
    """Решето Эратосфена: простой вариант"""

    m = [0, 0] + [1] * (n - 2)
    for i in range(2, int(n ** 0.5 + 1)):  # обход можно осуществлять до корня из n
        if m[i]:  # если не 0
            for j in range(i * i, n, i):  # заполняем все кратные этому числу индексы нулями (кроме самого числа)
                m[j] = 0
    res = [i for i in range(n) if m[i]]
    return res


c = time.time()
sieve(1000)
print(time.time() - c)

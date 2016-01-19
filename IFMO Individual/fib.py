import functools, sys

sys.setrecursionlimit(99999999)


@functools.lru_cache()
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(565))

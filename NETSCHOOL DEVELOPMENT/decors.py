import functools


def once(func):  # Запуск функции лишь единожды
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True
        inner.called = False
        return inner


def memoized(func):  # Запомиает значения функции и может убрать дополнительные вычисления
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args, kwargs
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return inner

import numpy as np

t0 = 0
h = 0.05
T = 10

A = np.array([1, 2, 3, 1, 3, 1, 4, 5, 6], dtype="float64").reshape(3, 3)
x = np.array([1, 1, 1], dtype="float64").reshape(3)


def f(x):
    return (-A).dot(x)


while t0 < T:
    K1 = h*f(x)
    K2 = h*f(x + K1/2)
    K3 = h*f(x + K2/2)
    K4 = h*f(x + K3)
    d = 1 / 6 * (K1*h + 2 * K2*h + 2 * K3*h + K4*h)
    x += d
    t0 += h

print(x)

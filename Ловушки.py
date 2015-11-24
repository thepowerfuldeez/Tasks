from math import sqrt

def is_in_circle(x0, y0, r, x, y):
    return (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r

def uravnenie_pryamoi(x1, y1, x2, y2):
    def y(x):
        return (x - x1) * (y2 - y1) / (x2 - x1) + y1
    return y

def tochki_peresechenia(x0, y0, r, y):
    return x0 + sqrt(r * r - (y - y0) * (y - y0)), x0 - sqrt(r * r - (y - y0) * (y - y0))



def replacing(a, x, y):
    a.replace(x,y)
    return a

with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(replacing(*fin.read().split("\n")), file = fout)
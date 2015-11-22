from math import factorial

with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(factorial(int(fin.read())), file=fout)
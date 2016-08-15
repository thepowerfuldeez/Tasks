def intodecimal(x):
    multiplier = 1
    x = list(x)
    ALPHABET = "ABCDEF"
    if x[0] == '-':
        multiplier = -1
        del x[0]
    for j in range(len(x)):
        if x[j] in ALPHABET:
            x[j] = str(ALPHABET.index(x[j]) + 10)

    return x[::-1], multiplier


def intobin(x):

    x, multiplier = intodecimal(x)

    table = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
             "1101", "1110", "1111"]

    dec = [ table[ int(i) ] for i in x ]

    return int("".join(dec[::-1])) * multiplier


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        print(intobin(fin.read()), file=fout)

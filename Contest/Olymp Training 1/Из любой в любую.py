def intodecimal(x, input_coding):
    return int(x, base=input_coding)


def intoselected(x, output_coding):
    dec = ""
    multiplier = 1
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = list(str(x))

    if x[0] == '-':
        multiplier = -1
        del x[0]

    x = int("".join(x))

    while x != 0:
        num = x % output_coding
        if num > 9:
            num = ALPHABET[num - 10]
        dec += str(num)
        x //= output_coding

    if multiplier < 0:
        dec += "-"

    return dec[::-1]


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        x = fin.readline().strip()
        input_coding, output_coding = [int(i) for i in fin.readline().strip().split()]
        print(intoselected(intodecimal(x, input_coding), output_coding), file=fout)

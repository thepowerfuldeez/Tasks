def intodecimal(x, input_coding):
    dec = 0
    multiplier = 1
    x = list(x)
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x[0] == '-':
        multiplier = -1
        del x[0]
    for j in range(len(x)):
        if x[j] in ALPHABET:
            x[j] = str(ALPHABET.index(x[j]) + 10)
    x = x[::-1]
    for i in range(len(x)):
        dec += (input_coding ** i) * int(x[i])
    return dec * multiplier

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
        print(intoselected(intodecimal(x, input_coding), output_coding), file = fout)

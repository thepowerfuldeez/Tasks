import re


def number_of_switches(word):
    n = 0
    eng_raskladka = 1

    for char in list(word):
        if re.match('[а-я]', char):
            if eng_raskladka != 0:
                n += 1
            eng_raskladka = 0

        elif re.match('[a-z]', char):
            if eng_raskladka != 1:
                n += 1
            eng_raskladka = 1

    return n


with open('input.txt') as fin:
    a = fin.read().strip()
    with open('output.txt', 'w') as fout:
        print((number_of_switches(a) + 1) * len(a), file=fout)

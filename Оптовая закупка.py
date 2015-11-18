with open('input.txt') as fin:
    N = int(fin.read())

mnogo = N // 144
sredne = (N - mnogo * 144) // 12
one = N - - mnogo * 144 - sredne * 12

with open('output.txt', 'w') as fout:
    print(one, sredne, mnogo, file = fout)
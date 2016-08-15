from itertools import permutations

N, S = map(int, input().split())
digits = [int(i) for i in input().split()]


for cmb in permutations(["+", "-"], r=N - 1):

    res = digits[0]

    for index, digit, char in zip(range(N), digits, cmb):
        if char == "+":
            res += digits[index + 1]
        elif char == "-":
            res -= digits[index + 1]

    if res == S:
        temp = [str(digits[0])]
        for i in range(N-1):
            temp.append(cmb[i])
            temp.append(str(digits[i+1]))
        new_res = "".join(temp) + "=" + str(S)
        break

if res == S:
    print(new_res)
else:
    print("No solution")
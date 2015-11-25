# 10010011
# 6
#
# 100
#
# 11100111001
# 7
#
# NO

def compress(s, index):
    if index > len(s) or index <= 1:
        return "".join(s)

    s = list(s)
    value = s[index - 1]

    if value == s[index - 2]:
        del s[index - 2]
        return compress(s, index - 1)
    elif value == s[index]:
        del s[index]
        return compress(s, index)
    else:
        del s[index - 1]
        return compress(s, index)


with open('destruction.in') as fin:
    s = fin.readline()
    index = int(fin.readline())
    with open('destrucion.out', 'w') as fout:
        result = compress(s, index)
        if len(result) > 1:
            print(result, file=fout)
        else:
            print("NO", file=fout)

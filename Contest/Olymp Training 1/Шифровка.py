def cycling(word):
    length = len([i for i in word if i.isalpha()])

    word = list(word)

    for i in range(len(word)):
        if word[i].isalpha():
            if 65 <= ord(word[i]) + length <= 90 or 97 <= ord(word[i]) + length <= 122:
                word[i] = chr(ord(word[i]) + length)
            else:
                word[i] = chr(ord(word[i]) + length - 26)

    return "".join(word)

with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        res = " ".join([cycling(word) for word in fin.read().split()])
        print(res, file=fout)

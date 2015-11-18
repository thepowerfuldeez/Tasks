def cycling(word):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    z = []
    for i in word:
        if i.isalpha():
            z.append(i)
    length = len(z)

    word = list(word)

    for char in range(len(word)):
        if word[char].isalpha():
            if word[char].isupper():
                word[char] = ALPHABET[(ALPHABET.index(word[char].lower()) + length) % len(ALPHABET)].upper()
            else:
                word[char] = ALPHABET[(ALPHABET.index(word[char].lower()) + length) % len(ALPHABET)].lower()

    return "".join(word)


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        res = " ".join([cycling(word) for word in fin.read().split()])
        print(res, file = fout)

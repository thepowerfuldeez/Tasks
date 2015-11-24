def wordlen(a):
    return len([i for i in a if i.isalpha()])


def notmat(a):
    count = 0
    for word in a.split():
        if wordlen(word) == 3:
            count += 1
    if count < 2:
        return a


with open('speech.in') as fin:
    N = int(fin.readline())
    with open('speech.out', 'w') as fout:
        for i in range(N):
            a = fin.readline()[:-1]
            if notmat(a):
                print(a, file=fout)
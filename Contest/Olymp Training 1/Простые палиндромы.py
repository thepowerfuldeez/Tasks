def isPalyndrome(a):
    return a[:len(a) // 2] == a[::-1][:-len(a) // 2]


def isPrime(a):
    i = 2
    while i < a:
        if a % i == 0: return False
        i += 1
    return True


def reshetoOfPrimePalyndromes(start, end):
    return [str(i) for i in range(start, end + 1) if isPrime(i) and isPalyndrome((str(i)))]


with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        a = reshetoOfPrimePalyndromes(*[int(i) for i in fin.read().strip().split()])
        if a:
            print(" ".join(a), file=fout)
        else:
            print(0, file=fout)

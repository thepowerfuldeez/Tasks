def isPalyndrome(a):
    a = str(a)
    return a[:len(a)//2] == a[::-1][:-len(a)//2]

def sumint(a):
    return sum(int(i) for i in list(str(a)))

def isNedoPalyndrome(a):
    return isPalyndrome(sumint(a)) and not isPalyndrome(a)

with open('palind.in') as fin:
    a, b = [int(i) for i in fin.read().split()]
    with open('palind.out', 'w') as fout:
        for i in range(a, b+1):
            if isNedoPalyndrome(i):
                print(i, file=fout)

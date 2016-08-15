def isPalindrome(a):
    return a[:len(a)//2] == a[::-1][:-len(a)//2]

with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        if isPalindrome(fin.read().strip().replace(" ", "")): print("YES", file = fout)
        else: print("NO", file = fout)
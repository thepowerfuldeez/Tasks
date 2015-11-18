from itertools import permutations as perm

def isPalindrome(a):
    return a[:len(a)//2] == a[::-1][:-len(a)//2]

sort = []

k = 0
a = list(input())
for i in perm(a):
    if isPalindrome(''.join(i)):
        sort.append(''.join(i))
        k += 1
sort = list(set(sort))
print(k)
print(sort)
import sys

sys.stdin = open("maxnumber.in")
sys.stdout = open("maxnumber.out", "w")

n = int(input())
a = [int(i) for i in input().split()]

print(sum(a))

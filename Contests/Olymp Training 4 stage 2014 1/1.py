import sys
import math

sys.stdin = open("pobeda.in")
sys.stdout = open("pobeda.out", "w")

a, b, c, d = map(int, input().split())
print(math.floor(math.sqrt(min(a, b) + min(c, d))))
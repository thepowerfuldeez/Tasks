import sys
import functools

sys.stdin = open("division.in")
sys.stdout = open("division.out", "w")

try:
    print(functools.reduce(lambda x, y: x // y, map(int, input().split())))
except:
    print("Na nol' delit' nel'zya!!!")

sys.stdin.close()
sys.stdout.close()
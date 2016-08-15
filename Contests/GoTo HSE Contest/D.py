import sys
sys.stdout = open("output.txt", "w")

s = open("input.txt").read()

ar = sorted(list(set(s)), key=lambda x: ord(x))
ar = list("".join("".join(ar).split()))
ar_map = {}
heights_ar = []

for letter in ar:
    height = s.count(letter)
    heights_ar.append([height, ar.index(letter)])
    ar_map[letter] = height

result = [[" "] * len(ar) for i in range(max(ar_map.values()))]
heights_ar.sort(key=lambda x: x[0], reverse=True)

for a in heights_ar:
    length = a[0]
    index = a[1]

    for i in range(length):
        result[i][index] = "#"

result = result[::-1]
for line in result:
    print("".join(line))
print("".join(ar))
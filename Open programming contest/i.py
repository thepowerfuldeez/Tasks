def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


s1 = "bear"
s2 = "deer"
s3 = "read"
s4 = "beard"

print(longest_common_substring(longest_common_substring(longest_common_substring(s1, s2), s3), s4))
print(longest_common_substring(longest_common_substring(longest_common_substring(s2, s3), s4), s1))
print(longest_common_substring(longest_common_substring(longest_common_substring(s3, s4), s1), s2))


# with open("input.txt") as fin, open("output.txt", "w") as fout:
#     n = int(fin.readline())
#
#     a = fin.readlines()
#
#     for i in range(n):
#         temp = []
#         for j in range(n):
#             l = longest_common_substring(a[i], a[j])
#             if l:
#                 temp.append(l)
#             else:
#                 temp.append("?")
#         print(min(temp), file=fout)

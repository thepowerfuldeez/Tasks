import re

pattern2 = re.compile("[+,-]")
pattern1a = re.compile("[+,\-,/,*]\s")
pattern1b = re.compile("[a-z]\s")

fin = open("b2.txt")
fout = open("b.txt", "w")

for line in fin:
    switcher = True

    if line.count(" ") == 0:
        switcher = False

    if switcher:
        for i in range(0, len(line), 2):
            if i + 2 >= len(line):
                switcher = False
                break
            if not (pattern1a.match(line[i:i + 2]) or pattern1b.match(line[i:i + 2])):
                switcher = True
                break

        if switcher:
            b = pattern2.split(line)
            if len(b) >= 2:
                if all(regex.count(" ") == 2 for regex in b[1:-1]):
                    if b[0].count(" ") == 1 and b[-1].count(" ") == 1:
                        switcher = False

            if switcher:
                print(0, file=fout)
            else:
                print(1, file=fout)

        else:
            print(1, file=fout)

    else:
        print(1, file=fout)

fin.close()
fout.close()

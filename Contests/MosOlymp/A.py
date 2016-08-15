with open("a2.txt") as fin:
    with open("a.txt", "w") as fout:
        for s in fin:
            print(eval(s[1:]), file=fout)
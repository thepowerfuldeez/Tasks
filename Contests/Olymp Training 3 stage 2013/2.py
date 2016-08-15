with open("cities.in") as fin, open("cities.out", "w") as fout:
    n = int(fin.readline())
    c_count = 0
    a = ""
    for line in fin:
        c_count += line.count("C")
        a += line
    c_count //= 2
    current_c = 0
    switcher = True
    b = []
    for s in a:
        if current_c < c_count:
            if s == "C":
                current_c += 1
            b.append("1")
        else:
            b.append("2")

    for i in range(n):
        print("".join(b[i * n:(i + 1) * n]), file=fout)

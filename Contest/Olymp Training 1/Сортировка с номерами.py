with open('input.txt') as fin:
    with open('output.txt', 'w') as fout:
        for index, value in enumerate(sorted([ z[3:] for z in fin.read().split("\n") ])):
            print("%d. %s" % (index+1, value), file = fout)
import sys

with open("input.txt") as fin:
    n, m, k = map(int, fin.readline().split())
    array = [[int(i) for i in el.split()] for el in fin]
    a, b = array[-1][0], array[-1][1]
    del array[-1]

road_end = a
current_company = 0
res = []
used = []


def first_search():
    global road_end
    global current_company
    road_end = a

    for element in array:
        if element[0] != road_end or element[1] != road_end:

            u = element[0]
            v = element[1]
            c = element[2]

            if u == road_end:
                road_end = v
            else:
                road_end = u
            current_company = c
            use(element)

            return element
    sys.exit(0)


def search():
    global road_end
    global current_company
    for element in array:
        if (road_end == element[0] or road_end == element[1]) and current_company == element[2] and element not in used:
            u = element[0]
            v = element[1]
            c = element[2]

            if u == road_end:
                road_end = v
            else:
                road_end = u
            current_company = c

            use(element)
            return element

    for element in array:
        if (road_end == element[0] or road_end == element[1]) and current_company == 0 and element not in used:
            u = element[0]
            v = element[1]
            c = element[2]

            if u == road_end:
                road_end = v
            else:
                road_end = u
            current_company = c

            use(element)
            return element


def use(element):
    if element[2] == 0:
        res.append(element[2])
    else:
        used.append(element)


# for i in range(k):
#     g_element = first_search()
#     while road_end != b:
#         g_element = search()
#
# with open("output.txt", "w") as fout:
#     print(len(res), file=fout)
#     print(" ".join(str(i) for i in res), file=fout)

x = first_search()
y = first_search()
y =  search()

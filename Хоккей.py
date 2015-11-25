def points(param1, param2):
    if param1 > param2:
        return 2, 0
    elif param2 > param1:
        return 0, 2
    elif param1 == param2:
        return 1, 1


def tiebreaker(a):
    sum1 = 0
    sum2 = 0
    for pair in a:
        sum1 += pair[0]
        sum2 += pair[1]

    if sum1 > sum2:
        return 1
    elif sum2 > sum1:
        return 2
    elif sum1 == sum2:
        return 0


def winner(a):
    command_points = [points(int(x.split()[0]), int(x.split()[1])) for x in a]

    sum1 = sum([a[0] for a in command_points])
    sum2 = sum([a[1] for a in command_points])

    if sum1 > sum2:
        return 1
    elif sum2 > sum1:
        return 2
    elif sum1 == sum2:
        tiebreaker(command_points)


with open('task.in') as fin:
    N = fin.readline()
    arr = fin.readlines()

    with open('task.out', 'w') as fout:
        print(winner(arr), file=fout)

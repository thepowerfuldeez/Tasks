def new_array(arr, N, iteration = 0):
    if iteration >= N:
        return
    new_arr = [0] * N
    for i in range(N):
        new_arr[i] = arr[(i + 1) % N]

    main_arr.append(new_arr)
    iteration += 1

    return new_array(new_arr, N, iteration)

def price(a):
    res = 0
    del a[0]
    length = 1
    
    while a:
        if len(a) == 1:
            res += length * a[0]
            break
        res += length * (a[0] + a[-1])
        length += 1
        del a[0]
        del a[-1]
    
    return res

fin = open('input.txt')

read = fin.read()
N = int(read.split()[0])
main_arr = []
new_array([int(i) for i in read.split()[1:]], N)

fin.close()

price_arr = []
for i in range(N):
    price_arr.append(price(main_arr[i]))
res = price_arr.index(min(price_arr)) + 2
with open('output.txt', 'w') as fout:
    print(res, file=fout)

def row_sum_odd_numbers(n):
    amount = 0
    for i in range(1,n):
        amount += i
    
    first = 1
    for i in range(amount):
        first += 2
        
    a = []
    for i in range(n):
        a.append(first)
        first += 2

    return sum(a)

print(row_sum_odd_numbers(int(input())))
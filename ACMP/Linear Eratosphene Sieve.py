def linear_sieve(N):

    lp = [0] * (N + 1)
    pr = []

    for i in range(2, N + 1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)
        j = 0
        while j < len(pr) and pr[j] <= lp[i] and pr[j] * i <= N:
            lp[i * pr[j]] = pr[j]
            j += 1

    return lp

print(linear_sieve(1000))
def primes(n):
    res = []
    for i in range(2, n):
        flag = True
        for j in range(2, int(n**0.5)+1):
            if i%j==0:
                flag = False
                break
        if flag:
            res.append(i)
    return len(res)


a = primes(1000000)
print(a)
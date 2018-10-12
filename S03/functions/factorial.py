def fact(n):
    res = 1
    while n > 0:
        res = res * n
        n -= 1

    return res

def combination(n, m):
    res = fact(n) / (fact(m) * fact(n-m))
    return res

res = combination(3, 1)

for i in range(5):
    print (combination(4, i), end='\t')

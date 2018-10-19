def zeta(s=2, n=100000):
    res = 0
    for i in range(1, n+1):
        res += 1 / (i ** s)
    return res

# function without any inputs will get
# s = 2 and N = 10e5 as default
print(zeta())

n_values = [10**i for i in range(1, 8)]
print(n_values)

pi_real = 3.141592653589793238462643383279

for n in n_values:
    val = zeta(n=n)
    pi_approximate = (val * 6) ** 0.5
    print(pi_approximate)

print(pi_real)

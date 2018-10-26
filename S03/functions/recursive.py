def fact(n):
    if not type(n) == int:
        raise ValueError
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fact(10.1))
# for i in range(10):
#     print(fib(i))
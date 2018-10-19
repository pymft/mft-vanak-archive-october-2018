# def fun(x, n=2, m=1):
#     return m * (x ** n)

def fun(x, **kwargs):
    n = kwargs.get('n', 2)
    m = kwargs.get('m', 1)

    return m * (x ** n)

def length(x, y, p=2):
    return (x ** p + y ** p) ** (1/p)

print(fun(10))
print(fun(10, n=10))
print(fun(10, n=10, m=2))
print(fun(10, m=2, n=10, mode='whatever'))

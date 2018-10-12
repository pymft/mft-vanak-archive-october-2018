# y = f(x)
# z = f(x, y)

# f(x) = x**2

def times_two(n):
    res = 2 * n
    return res

print(type(times_two))
# print(type(times_two(2)))
value1 = times_two(1)
value2 = times_two(2)

print(value1, value2)

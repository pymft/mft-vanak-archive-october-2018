def power_n(n):
    def inner(x):
        return x**n

    return inner


# <b>hello</b>
# <i>hello</i>

f2 = power_n(2)
f5 = power_n(5)

print("5 ^ 2 = ", f2(5))
print("2 ^ 5 = ", f5(2))

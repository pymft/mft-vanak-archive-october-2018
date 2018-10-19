import sys


def fib_generator(n):
    a, b = 1, 1
    yield a
    yield b
    n = n - 2
    while n >=0:
        n -= 1
        a, b = b, a + b
        yield b


gen1 = fib_generator(100)
gen2 = fib_generator(100)
print(next(gen1))   # expected output  --> 1
print(next(gen1))   # expected output  --> 1
print(next(gen2))   # expected output  --> 1
print(next(gen1))   # expected output  --> 2
print(next(gen1))   # expected output  --> 3
print(next(gen2))   # expected output  --> 1
#
# counter = 0
# s= 0
# for i in gen:
#     counter += 1
#
#     print(counter, i)
def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4

g = simple_generator()
print(g)

for i in g:
    print(i)
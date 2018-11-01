class MyClass:
    pass


class NewClass:
    x = 10
    y = 20
    f = lambda n: n*2

c1 = MyClass()
c2 = MyClass()

c1.x = 10    # instance variable
c1.y = 20

# attr have not set for c2 !!
print(c2.x)  # raise Error

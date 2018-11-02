class MyTestClass:
    def __init__(self, x):
        self.x = x

    def __getattribute__(self, item):
        print("recv. req to show {} item".format(item))
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return None

class MyTestClassNew:
    def __init__(self, y):
        self.y = y



m1 = MyTestClass(1)
m2 = MyTestClassNew(1)

print(m1.x)
print(m1.y)



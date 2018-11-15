class MyClass:
    instance = []
    # Python Unlocked! <Packed pub>

    def __new__(cls, a):
        print('__new__ method called', a)
        return super().__new__(cls)

    def __init__(self, a):
        print('__init__ method called', a)

        self.__attrib = a
        self.instance.append(self)
        # self.__class__.instance.append()

    @classmethod
    def count(cls):
        return len(cls.instance)


    @property
    def attrib(self):
        return self.__attrib

    @attrib.setter
    def attrib(self, value):
        if isinstance(value, int):
            self.__attrib = value
        else:
            raise ValueError

    def __add__(self, other):
        pass

    # __mul__, __div__, __sub__
    # __not__, __neg__

    def __repr__(self):
        text = str(id(self))
        return text


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def length(x, y):
        return (x**2 + y**2)**0.5











c = MyClass(10)
print(c)
d = MyClass(0)
print(d)
#
# c + d
# c.__add__(d)
# MyClass.__add__(c, d)
#
# c.attrib
# MyClass.var = 100
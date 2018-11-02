class Vector:
    instance = []

    def __init__(self, x, y):

        self.__x = x
        self.__y = y

        self.__length = (x ** 2 + y ** 2) ** 0.5

    def __repr__(self):
        out = "||<{}, {}>|| -> {} : {}".format(
            self.x, self.y, self.length)
        return out

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        self.__length = (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__y = value
        self.__length = (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        ratio = value / self.__length
        self.__x = ratio * self.x
        self.__y = ratio * self.y
        self.__length = value


# turn to immutable?
vec = Vector(3, 4)
print(vec)
# print(vec.__new_var)
print(vec.length)

vec.length = 10
print(vec)
print(vec.length)
print(Vector.__dict__.keys())
print(vec.__dict__.keys())
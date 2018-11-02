class Vector:
    instance = []
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        out = "||<{}, {}>|| -> {}".format(
            self.x, self.y, self.length)
        return out

    @property
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @length.setter
    def length(self, value):
        ratio = value / self.length
        self.x = ratio * self.x
        self.y = ratio * self.y


# turn to immutable?
vec = Vector(3, 4)
print(vec)
print(vec.length)

vec.length = 10
print(vec)
print(vec.length)
print(Vector.__dict__.keys())
print(vec.__dict__.keys())
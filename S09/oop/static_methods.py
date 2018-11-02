def length(x, y):
    return (x ** 2 + y ** 2) ** 0.5

class Vector:
    instance = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def static_length(x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(3, 4)
v2 = Vector(4, 3)

print(v1.length)
print(v2.length)
print(v1.static_length)
print(v2.static_length)
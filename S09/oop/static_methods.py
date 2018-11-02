def length(x, y):
    return (x ** 2 + y ** 2) ** 0.5


class Vector:
    instance = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.instance.append(self)

    @staticmethod
    def static_length(x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @classmethod
    def count(cls):
        return len(cls.instance)


v1 = Vector(3, 4)
print("access instances from class    ", Vector.instance)
print("access instances from instance ", v1.instance)
v2 = Vector(4, 3)
print("access instances from class    ", Vector.instance)
print("access instances from instance ", v2.instance)

print(Vector.count)
print(v1.count)
print(v1.length)
#
# print(v1.length)
# print(v2.length)
# print(v1.static_length)
# print(v2.static_length)
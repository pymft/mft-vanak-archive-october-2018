class Vector:
    def __init__(self, *args):
        self.dim = args

    def __mul__(self, k):
        dim = [i * k for i in self.dim]
        return Vector(*dim)

    def __add__(self, other):
        args = [s + o for s, o in zip(self.dim, other.dim)]
        return Vector(*args)

    def length(self):
        res = [i ** 2 for i in self.dim]
        return sum(res) ** 0.5

    def __repr__(self):
        return str(self.dim)


class Vector2D(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y)



v_new = Vector2D(10, 20)
print(v_new.length())
print(v_new.x, v_new.y, v_new.dim)
print(v_new)



# v1 = Vector(3, 4, 10, 20)
# print(v1)
# v2 = v1 * 2
# print(v2)
# # Vector.__add__(v1, v2)
# # v1.__add__(v2)
# # v1 + v2
# v3 = v2 + v1  # v2.__add__(v1)
# print(v3)
# print(v2.length())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def mul(self, k):
        x_new = self.x * k
        y_new = self.y * k
        return Vector(x_new, y_new)

    def length(self):
        return (self.x**2 + self.y**2)**0.5


# def mul(vec, k):
#     x_new = vec.x * k
#     y_new = vec.y * k
#     new_vec = Vector(x_new, y_new)
#     return new_vec
#



v1 = Vector(10, 20)
v2 = Vector(3, 4)

# v3 = mul(v1, 3)
v3 = v2.mul(3)
print(v2.x, v2.y, v2.length())
print(v3.x, v3.y, v3.length())


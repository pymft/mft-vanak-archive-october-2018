class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __sub__, __mul__, __div__, __pow__,
    # __or__, __and__,
    # __in__
    # __not__, __neg__
    #

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return (x_new, y_new)
# f(o)
# o.f()

vec = Vector(10, 20)
vec2 = Vector(30, 20)

vec + vec2    # vec.__add__(vec2)  # Vector.__add__(vec, vec2)
print(vec.x, vec.y)
vec.length()
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        s = 'Rectangle\n'
        s += '+' + '--' * self.width + '+\n'
        for i in range(self.height):
            s += '+' + '  ' * self.width + '+\n'
        s += '+' + '--' * self.width + '+\n'
        return s


class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        super().__init__(self.a, self.a)

    def __repr__(self):
        text = super().__repr__()
        return text.replace('Rectangle', 'Square')


s = Square(4)
print(s)
print(s.area(), s.perimeter())


# r = Rectangle(3, 3)
# print(r.area(), r.perimeter())
# print(r)
class MyIterator:
    def __init__(self, *args):
        self.dim = list(args)

    def __getitem__(self, item):
        return self.dim[item]

    def __setitem__(self, key, value):
        self.dim[key] = value

    def __repr__(self):
        return "MyIterator: {}".format(self.dim)


m = MyIterator(1, 2, 3, 4)
print(m[1])
print(m)
m[1] = 100
print(m[1])
print(m)

# lst = [1, 2, 3]
# f = lambda x: x**2
#
# lst[1]    # lst.__getitem__(1)
#
# lst[1] = 10    # lst.__setitem__(1, 10)
#                list.__setitem__(lst, 1, 10)
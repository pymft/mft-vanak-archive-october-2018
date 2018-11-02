class MyIterator:
    def __init__(self, *args):
        self.dim = list(args)

    def __getattribute__(self, item):
        if item[0] == '_' and item[1:].isdigit:
            indx = int(item[1:])
            return self.dim[indx]
        return super().__getattribute__(item)


m = MyIterator(1, 2, 3, 4, 5)
print(m._4)

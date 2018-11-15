class Singleton:
    _instances = []

    def __new__(cls, param):
        params = [o.param for o in cls._instances]

        if param in params:
            i = params.index(param)
            return cls._instances[i]

        return super().__new__(cls)

    def __init__(self, param):
        self.param = param
        self._instances.append(self)


a = Singleton(100)
b = Singleton(200)
c = Singleton(300)
d = Singleton(100)

for obj in [a, b, c, d]:
    print(obj, id(obj))






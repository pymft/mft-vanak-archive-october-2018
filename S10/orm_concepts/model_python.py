class Person:
    _instances = []

    def __init__(self, firstname, lastname, age=None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self._instances.append(self)

    @classmethod
    def search(cls, f):
        return filter(f, cls._instances)

    def __repr__(self):
        return "{self.firstname} {self.lastname}".format(self=self)


f = lambda x: x.age < 26
p1 = Person('John', 'Smith', 30)
p2 = Person('John', 'Lock', 20)
res = Person.search(f)
res = list(res)
print(res)

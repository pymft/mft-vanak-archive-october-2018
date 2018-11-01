class Whatever:
    instances = []

    def __init__(self, name):
        names = [a.name for a in self.instances]
        if name in names:
            raise Exception
        self.name = name
        self.instances.append(self)


# v = Whatever()
# print(Whatever.instances)
# Whatever()
# print(Whatever.instances)
# x = Whatever()
# print(Whatever.instances)

class Person:
    def __init__(self, name, age):
        print('Person {} started to initiate --> {}'.format(name, self.__class__))

        self.name = name
        self.age = age


    def say_something(self):
        print("{} says something".format(self.name))


class Employee(Person):
    def __init__(self, name, age, pid):
        print('Employee {} started to initiate --> {}'.format(name, self.__class__))
        super().__init__(name, age)
        self.pid = pid

    def __call__(self):
        print("Yoohoo I am here ")
        
    def say_something(self):
        super().say_something()
        print("{} says something: {}".format(self.name, self.pid))


p1 = Person('John', 30)
print('-'*20)
e1 = Employee('John', 30, 123123123)
# e2 = Employee('Emma', 27, 234234324)
e1()


#
# p1.say_something()
# p2.say_something()

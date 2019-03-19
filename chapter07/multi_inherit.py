class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

# 加上runnable和flyable
class Runnable():
    def run(self):
        print('Running....')


class Flyable():
    def fly(self):
        print('Flying....')


class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass
# 通过多重继承,一个子类就可以同时获得多个父类的所有功能

batman = Bat()
batman.fly()

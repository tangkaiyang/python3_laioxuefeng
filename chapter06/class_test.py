# class Animal():
#     pass
#
# a = Animal()
#
# class Dog(Animal):
#     pass
#
# d = Dog()
#
# class Husky(Dog):
#     pass
#
# h = Husky()
#
# print(isinstance(h, Husky))
# print(isinstance(h, Dog))
# print(isinstance(h, Animal))
# print(isinstance(d, Dog) and isinstance(d, Animal))
# print(isinstance(d, Husky))
# print(dir(h))

class MyObject():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x')  #有属性x吗
obj.x
hasattr(obj, 'y') # 有属性y吗
setattr(obj, 'y', 19)# 设置一个属性y
hasattr(obj, 'y')
getattr(obj, 'y') # 获取属性y
# 如果试图获取不存在的属性,抛AttributeError错误
# 可以传入default参数,如果属性不存在,返回默认值
getattr(obj, 'z' , 404) # 获取属性z,如果不存在,返回默认值404
getattr(obj, 'power') # 获取属性power(对象的方法)

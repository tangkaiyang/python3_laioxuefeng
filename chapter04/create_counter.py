# -*- coding:UTF-8 -*-

# def count():
#     def f(j):
#         def g():
#             return j * j
#
#         return g
#
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs


# f1, f2, f3 = count()
# print(f1(), f2(), f3())

#
# def createCounter():
#     s = [0]
#     def counter():
#         s[0] = s[0] + 1
#         return s[0]
#     return counter
#
# counterA = createCounter()
# counterB = createCounter()
# print(counterA(), counterB())

print(type(iter([1, 2, 3])))


def createCounter():
    def counter():
        x = 1
        while True:
            yield x
            x += 1
    def func():
        return next(c)
    c = counter()
    return func

counterA = createCounter()
counterB = createCounter()
print(counterA(), counterA())
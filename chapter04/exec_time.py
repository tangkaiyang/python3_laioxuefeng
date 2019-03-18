# -*- coding:UTF-8 -*-
import time, functools

# def metric(fn):
#     global start_time
#     start_time = time.time()
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         print("pass")
#         r = fn(*args, **kw)
#         print('%s executed in %s ms' % (fn.__name__, (time.time() - start_time) * 1000))
#         return r
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# f = fast(11, 22)
# print(f)

# def log(text="pass"):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print(text)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @log()
# def add(x, y):
#     return x + y
#
# add(1,2)

def log(text):
    if callable(text) == False:
        def dera(func):
            def wraps():
                print("Now is %s for sleeping" % text)
                return func()
            return wraps
        return dera
    else:
        def wraps():
            return text()
        return wraps

@log
def now1():
    print("It's time to go to bed?")

@log('too late')
def now2():
    print("Go to bed now please?")

now1()
now2()
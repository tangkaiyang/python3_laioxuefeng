# -*- coding:UTF-8 -*-
import functools

# def log(func):
#     @functools.wraps(func)
#     def decorator(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return decorator


def log(text="execute"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    print('2015-3-25')


print(now())
print(now.__name__)
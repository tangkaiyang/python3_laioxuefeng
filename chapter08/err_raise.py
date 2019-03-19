import pdb


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    pdb.set_trace()
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
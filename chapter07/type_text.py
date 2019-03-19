# 先创建函数
def fn(self, name='world'):
    print('Hello, %s.' % name)


# 创建Hello class
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))

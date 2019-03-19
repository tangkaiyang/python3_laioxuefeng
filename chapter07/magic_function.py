class Student():
    def __init__(self, name):
        self.name = name

    # 定义__str__在打印时作用
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __call__(self):
        print('My name is %s' % self.name)


class Fib():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Chain():
    def __init__(self, path=""):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# f = Fib()
# print(f[1])
# print(f[1:4])
# print(Student('Michael').score)
# print(Chain("login").status.user.timeline.list)
s = Student('Michael')
s()
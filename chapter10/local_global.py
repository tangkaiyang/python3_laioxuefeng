
def fun():
    num2 = 3
    def fun2():
        nonlocal num2
        num2 *= 2
        print('num2 = ', num2)
    return fun2()


fun()
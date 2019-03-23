#  -*- coding:UTF-8 -*-
"""
计算圆周率可以根据公式:
利用Python提供的itertools模块,我们来计算这个序列的前N项和:
"""
import itertools


def pi(N):
    '计算pi的值'
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9 ... count(start, step)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: 添加正负号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...  cycle(list)
    # step 4: 求和 next()/next() 求和
    odd = itertools.count(1, 2)
    cs = itertools.cycle([4, -4])
    sum = 0
    for i in range(N):
        sum = sum + (next(cs)/next(odd))

    return sum


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
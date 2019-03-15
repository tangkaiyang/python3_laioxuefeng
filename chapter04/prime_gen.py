"""
埃氏筛法:
从2开始,依次筛掉2, 3, .....的倍数,
最后得到所以素数
"""


# 大于2的偶数肯定不是素数,筛掉2的倍数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义生成器
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

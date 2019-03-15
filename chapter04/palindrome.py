# -*- coding:UTF-8 -*-
"""
回数,倒过来也是我自己
"""

def is_palindrome(n):
    # l = str(n)
    # for i in range(len(l) // 2 + 1):
    #     if l[i] != l[-(i + 1)]:
    #         return
    #     continue
    # return n
    return str(n) == str(n)[::-1]

print(list(filter(is_palindrome, range(1, 200))))



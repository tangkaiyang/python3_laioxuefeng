# -*- coding:UTF-8 -*-
"""
请尝试写一个验证Email地址的正则表达式.版本一应该可以验证出类似的Email:
someone@gmail.com
bill.gates@microsoft.com
版本二可以提取出带名字的Email地址:
<Tom Paris>tom@voyayer.org => Tom Paris
bob@example.com => bob
"""


import re
# def is_valid_email(addr):
#     return re.match(r'^[\w.]+@\w+.[a-z]+$', addr)
#
#
# # 测试
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print(is_valid_email('someone@gmail.com'))
# print(is_valid_email('bill.gates@microsoft.com'))
# print(is_valid_email('bob#example.com'))
# print(is_valid_email('mr-bob@example.com'))

#
# def name_of_email(addr):
#     type1 = re.match(r'^([\w.]+)@\w+.[a-z]+$', addr)
#     type2 = re.match(r'^\<([A-Za-z ])\> [\w.]+@\w+.[a-z]+$', addr)
#     if type1:
#         return type1.groups()
#     elif type2:
#         return type2.groups()
#     else:
#         return
#
# # 测试:
def name_of_email(addr):
    rr = re.compile(r'^\<?(\w+\s?\w+)\>?\.?\s?\w*?(\@)(\w+)(\.\w+$)')
    try:
        return rr.match(addr).group(1)
    except AttributeError as ae:
        return False
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

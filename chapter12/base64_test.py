#  -*- coding:UTF-8 -*-
# import base64
#
# be = base64.b64encode(b'binary\x00string')
# print(be)
# bd = base64.b64decode(be)
# print(bd)
# so = b'i\xb7\x1d\xfd\xef\xff'
# bd2 = base64.b64encode(so)
# bd3 = base64.urlsafe_b64encode(so)
# bd4 = base64.urlsafe_b64decode('abcd--__')
# print(bd2)
# print(bd3)
# print(bd4)
"""
练习:
请写一个能处理掉=的base64编码函数:
"""
import base64
def safe_base64_decode(s):
    pass
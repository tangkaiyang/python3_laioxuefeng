#  -*- coding:UTF-8 -*-

import hashlib
"""
根据用户输入的口令,计算出存储在数据库中的MD5口令
存储MD5的好处是即使运维人员能访问数据库,也无法获知用户的明文口令
设计一个验证用户登录的函数,根据用户输入的口令是否正确,返回True或False
"""


# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf8'))
#     return md5.hexdigest()

#
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#
#
# def login(user, password):
#     if user in db and db[user] == calc_md5(password):
#         return True
#     else:
#         return False

# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')


"""
根据用户输入的登录名和口令模拟用户注册,计算更安全的MD5
然后,根据修改后的MD5算法实现用户登录的验证
"""
# db = {}
#
#
# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')


import random


def get_md5(s):
    return hashlib.md5(s.encode('utf8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
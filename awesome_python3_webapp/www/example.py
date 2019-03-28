# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 17:22
# @Author   : tangky
# @Site     : 
# @File     : example.py
# @Software : PyCharm

import orm
from models import User, Blog, Comment

async def example():
    await orm.create_pool(user='root', password='123456', database='awesome')
    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')
    await u.save()

example()
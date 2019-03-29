# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 17:22
# @Author   : tangky
# @Site     : 
# @File     : example.py
# @Software : PyCharm
import asyncio
import orm
from models import User, Blog, Comment


async def example(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(example(loop))

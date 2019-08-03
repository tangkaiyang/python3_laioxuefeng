# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/8/3 15:36
# @Author   : tangky
# @Site     : 
# @File     : test.py
# @Software : PyCharm

import asyncio

import orm
from models import User, Blog, Comment


async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='Test', email='test@qq.com', passwd='123456', image='about:blank')
    await u.save()
    # 添加到数据库后需要关闭连接池,否则报错
    orm.__pool.close()
    await orm.__pool.wait_closed()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()

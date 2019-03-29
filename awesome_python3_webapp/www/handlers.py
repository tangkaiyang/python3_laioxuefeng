# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 11:52
# @Author   : tangky
# @Site     : 
# @File     : handlers.py
# @Software : PyCharm

"""
url handlers
"""
import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    summary = ''
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

    # users = await User.findAll()
    # return {
    #     '__template__': 'test.html',
    #     'users': users
    # }


"""
Day9: 编写API
Roy Fielding,2000,REST:Representational State Transfer,取代了SOAP,称为Web API的标准
一个URL返回的不是HTML,而是机器能直接解析的数据,这个URL就可以看成是一个Web API
REST就是一种设计API的模式.
最常用的数据格式是JSON.由于JSON能直接被JavaScript读取,以JSON格式编写的REST风格的API具有简单,易读,易用的特点.
由于API就是把Web APP的功能全部封装了,
所以,通过API操作数据,可以极大地把前端和后端的代码隔离,使得后端代码易于测试,前端代码编写更简单.
"""


# 获取注册用户的API
@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)

"""
Day10: 用户注册和登录
用户注册可以通过API实现:
"""

import re
_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]_){1,4}$')

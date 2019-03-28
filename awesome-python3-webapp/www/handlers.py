# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 10:43
# @Author   : tangky
# @Site     : 
# @File     : handlers.py
# @Software : PyCharm

"""
MVC模式(Model-View-Controller)是软件工程中一种软件架构模式,
把软件系统分为三个基本部分:模型(Model),视图(View)和控制器(Controller).
"""

from models import User
from coroweb import get
import asyncio

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
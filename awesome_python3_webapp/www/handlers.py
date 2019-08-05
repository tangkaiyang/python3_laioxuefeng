# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 11:52
# @Author   : tangky
# @Site     : 
# @File     : handlers.py
# @Software : PyCharm

"""
编写MVC
Model-View-Controller
"""
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from models import User
from coroweb import get


@get('/')
async def index(request):
    users = await User.findAll()
    logging.info(users)
    return {
        '__template__': 'test.html',
        'users': users,
    }



# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 13:54
# @Author   : tangky
# @Site     : 
# @File     : app.py.py
# @Software : PyCharm

"""
网站骨架
"""
import logging

logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


async def index(request):
    return web.Response(body=b"<h1>Awesome Website</h1>", content_type="text/html")


def init():
    app = web.Application()
    app.router.add_get(r'/', index)
    web.run_app(app, host='127.0.0.1', port=9000)


if __name__ == '__main__':
    init()

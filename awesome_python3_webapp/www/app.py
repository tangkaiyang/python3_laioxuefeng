# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 13:54
# @Author   : tangky
# @Site     : 
# @File     : app.py.py
# @Software : PyCharm

"""
网站骨架

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
"""
import logging
import os
import json
import time
from datetime import datetime

import asyncio
from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs
import orm
from coroweb import add_routes, add_static

logging.basicConfig(level=logging.INFO)


## 初始化jinja2的函数
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape=kw.get('autoescape', True),
        block_start_string=kw.get('block_start_string', '%{'),
        block_end_string=kw.get('block_end_string', '}%'),
        variable_start_string=kw.get('variable_start_string', '{{'),
        variable_end_string=kw.get('variable_end_string', '}}'),
        auto_reload=kw.get('auto_reload', True),
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env


# 以下是middleware,可以把通用的功能从每个URL处理函数中拿出来集中放到一个地方
# URL处理日志工厂
async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return await handler(request)
    return logger

# 认证处理工厂


# 数据处理工厂
async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startwith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startwith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return await handler(request)
    return parse_data

# 响应返回处理工厂
async def response_factory(app, handler):
    async def response(request):
        logging.info('Request handler...')
        r = await handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):

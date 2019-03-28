# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 13:54
# @Author   : tangky
# @Site     : 
# @File     : app.py.py
# @Software : PyCharm

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='127.0.0.1', port=8000)

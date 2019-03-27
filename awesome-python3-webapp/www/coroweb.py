#  -*- coding:UTF-8 -*-

# 搭建web框架

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web

# apis是处理分页的模块
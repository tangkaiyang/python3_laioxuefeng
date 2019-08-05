# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 13:17
# @Author   : tangky
# @Site     : 
# @File     : config_default.py
# @Software : PyCharm

"""
一个网站应用运行时都需要读取配置文件,一般包括数据库的用户名,口令等.默认的配置文件应该符合本地开发环境
"""
configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'awesome',
    },
    'session': {
        'secret': 'Awesome',
    }
}
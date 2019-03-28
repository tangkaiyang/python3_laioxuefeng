# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一个网站应用运行时都需要读取配置文件,一般包括数据库的用户名,口令等.
默认的配置文件应该符合本地开发环境,
"""
cofigs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
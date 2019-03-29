# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 13:17
# @Author   : tangky
# @Site     : 
# @File     : config_default.py
# @Software : PyCharm

"""
编写配置文件,
有了Web框架和ORM框架,我们就可以开始装配App了
通常,一个Web App在运行时都需要读取配置文件,比如数据库的用户名,口令等,在不同的环境中运行时,Web APP可以通过读取不同的配置文件
来获得正确的配置
由于Python本身语言简单,完全可以直接用Python源代码来实现配置,而不需要再解析一个单独的.properties或.yaml等配置文件
默认的配置文件应该完全符合本地开发环境,这样,无需任何配置,就可以立即启动服务器.
默认的配置文件命名为config_default.py
"""
configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'db': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}
"""
但是,如果要部署到服务器时,通常需要修改数据库的host等信息,直接修改config_default.py不是一个好方法,更好的方法是
编写一个config_override.py,用来覆盖某些默认配置:
"""
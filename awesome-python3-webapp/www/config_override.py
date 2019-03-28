# !/user/bin/env python3
# -*- coding:UTF-8 -*-

"""
当网站部署到服务器时,通常需要修改数据库的host信息,直接修改config_default.py不是一个好方法,
更好的方法是编写一个config_override.py,用来覆盖某些默认设置
本地测试时不需要编写创建config_override.py
"""

configs = {
    'db': {
        'host': '192.168.0.100'
    }
}
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 13:24
# @Author   : tangky
# @Site     : 
# @File     : config_override.py
# @Software : PyCharm


# 当网站部署到服务器时,通常需要修改数据库的host等配置信息,直接修改config_default.py不合适,
# 编写config_override.py覆盖配置
configs = {
    'db': {
        'host': '127.0.0.1'
    }
}
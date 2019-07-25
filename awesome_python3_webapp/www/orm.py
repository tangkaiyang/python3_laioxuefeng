# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/28 16:17
# @Author   : tangky
# @Site     : 
# @File     : orm.py.py
# @Software : PyCharm

import asyncio, aiomysql, logging


def log(sql, args=()):
    logging.info("SQL: %s" % sql)


# 建立连接池
async def create_pool(loop, **kwargs):
    logging.info('create database connections pool......')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', 3306),
        user=kwargs['user'],
        password=kwargs['password'],
        db=kwargs['db'],
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        minsize=kwargs.get('minsize', 1),
        maxsize=kwargs.get('maxsize', 10),
        loop=loop,
    )


# SELECT, 用函数select执行传入SQL语句和SQL参数
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


# 注意要始终使用带参数的SQL,而不是自己拼接的SQL字符串,这样可以防止SQL注入攻击

# INSERT,UPDATE,DELETE,使用通用的execute()函数,都需要相同的参数,以及返回一个整数表示影响的行数
async def execute(sql, args):
    log(sql)
    global __pool
    with (await __pool) as conn:
        try:
            cur = await conn.cursor(aiomysql.DictCursor)
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
        except BaseException as e:
            raise
        return affected


# ORM,首先定义所有ORM映射的基类Model
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]


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
    global __pool
    __pool = await aiomysql.create_pool(
        loop=loop,
        host=kwargs.get('host', 'localhost'),
        port=kwargs.get('port', 3306),
        user=kwargs['user'],
        password=kwargs['passwd'],
        db=kwargs['db'],
        charset=kwargs.get('charset', 'utf8'),
        autocommit=kwargs.get('autocommit', True),
        minsize=kwargs.get('minsize', 1),
        maxsize=kwargs.get('maxsize', 10),
    )
    logging.info('create database connections pool......')



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


# 注意到Model只是一个基类,要将具体的子类如User的映射信息读取出来需要通过metaclass:ModelMetaclass.这样,任何继承子Model的类(比
# 如User),会自动通过ModelMetaclass扫描映射关系,并存储到自身的类属性如__table__,__mappings__中
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 排除Model类本身
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # 获取table名称
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        # 获取所有Field和主键名
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info(' found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    if primaryKey:
                        raise RuntimeError('Duplicate primary key for fields: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句
        attrs['__select__'] = 'SELECT `%s`, %s FROM `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'INSERT INTO `%s` (%s, `%s`) VALUES(%s)' % (
            tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'UPDATE `%s` SET %s WHERE `%s`=?' % (
        tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'DELETE FROM `%s` WHERE `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


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
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value
    # 添加class方法,可以让所有子类调用class方法
    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        # find all objects from where caluse
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                sql.append(str(limit))
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                sql.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        print("#########sql:%s and args:%s############" % (sql, args))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        # find number by select and where
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        # find object by primary key
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])
    # 添加实例方法,就可以让所有子类调用实例方法
    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warning('failed to insert record: affected rows: %s' % rows)
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warning('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warning('failed to remove by primary key: affected rows: %s' % rows)



class Field:
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return "<%s, %s:%s>" % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

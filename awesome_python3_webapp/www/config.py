# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 13:25
# @Author   : tangky
# @Site     : 
# @File     : config.py
# @Software : PyCharm

"""
优先从config_override.py读取
所有配置读取到统一的config.py中,将之转化成可读的字典
"""
import config_default


class Dict(dict):
    """
    Simple dict but support access as x.y style.
    """

    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# defaults与override合并,override覆盖
def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
    return D


configs = config_default.configs

try:
    import config_override

    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)

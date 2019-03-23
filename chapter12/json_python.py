#  -*- coding:UTF-8 -*-

"""
利用urllib读取JSON,然后将JSON解析为Python对象:
"""
from  urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf8')
        # Data = data.decode('utf8')
        result = json.loads(data)

        return result



print(fetch_data('http://news-at.zhihu.com/api/4/news/latest'))
# -*- coding:UTF-8 -*-

"""
假设你获取了用户输入的日期和时间如2015-1-21 9:01:30,以及一个时区信息如UTC+5:00,均为str,请编写一个函数将
其转换为timestamp
"""
from datetime import datetime, timedelta, timezone
import re


# 先转成UTC+0:00时区的datetime,然后转为timestamp

def to_timestamp(dt_str, tz_str):
    h = int(re.match(r'UTC(.+)\:00', tz_str).group(1))
    localtimezone = timezone(timedelta(hours=h))
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt_utc = dt.replace(tzinfo=localtimezone)
    return dt_utc.timestamp()


print(to_timestamp('2015-6-1 08:10:30', 'UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30', 'UTC-9:00'))

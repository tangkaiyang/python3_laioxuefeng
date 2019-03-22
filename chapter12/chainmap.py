#  -*- coding:UTF-8 -*-

from collections import ChainMap
import os, argparse

# 构造缺省参数:
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }
#
# # 构造命令行参数:
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = {k: v for k, v in vars(namespace).items() if v}
#
# # 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)
#
# # 打印参数
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
cm = ChainMap(baseline, adjustments)
for k, v in cm.items():
    print(k, v)
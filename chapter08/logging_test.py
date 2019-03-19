import logging
logging.basicConfig(level=logging.INFO)  # 未配置此行查看不到输出文本

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
"""
logging.info()就可以输出一段文本.运行,发现除了ZeroDivisionError,没有任何信息
logging,允许你指定记录信息的级别,有debug,info,warning,error等几个级别,当我们指定level=INFO时,logging.debug就不起作用了
同理,指定level=WARNING后,debug和info就不起作用了
logging的另一个好处是通过简单的配置,一条语句可以同时输出到不同的地方,比如console和文件
"""
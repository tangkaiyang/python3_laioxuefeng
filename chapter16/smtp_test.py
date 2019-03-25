#  -*- coding:UTF-8 -*-

# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python..', 'plain', 'utf-8')
# # 输入Email地址和口令
# from_addr = '945541696@qq.com'
# password = 'oosxjwueowvbbbje'
# # 输入收件人地址:
# to_addr = 'm17757989076@163.com'
# # 输入smtp服务器地址
# smtp_server = 'smtp.qq.com'
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # smtp协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '945541696@qq.com'
password = 'oosxjwueowvbbbje'
to_addr = 'm17757989076@163.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候.....', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
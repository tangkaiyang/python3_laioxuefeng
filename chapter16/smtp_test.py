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
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


to_addr = 'tangkaiyang233@gmail.com'
password = 'rwubydequmpvbfge'
# password = 'tangkaiyang123'
# to_addr = 'm17757989076@163.com'
# to_addr = 'tangky@lrwanche.com'
from_addr = '945541696@qq.com'
smtp_server = 'smtp.qq.com'
# smtp_server = 'smtp.gmail.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#                '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#                '</body></html>', 'html', 'utf-8') # 发送HTML,将参数为html
# 邮件对象
# msg = MIMEMultipart()
msg = MIMEMultipart('alternative') # 加subtype二选一

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候.....', 'utf-8').encode()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# 邮件正文是MIMEtext:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 将图片附件插入正文
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#                     '<p><img src="cid:0"></p>' +
#                     '</body></html>', 'html', 'utf-8'))
# 添加附件就是加上一个MIMEBase,从本地读取一个图片
# with open('code.png', 'rb') as f:
#     # 设置附件的MIME和文件名,这里是png类型
#     mime = MIMEBase('image', 'png', filename='code.png')
#     # 加上必要的头信息
#     mime.add_header('Content-Disposition', 'attachment', filename='code.png')
#     mime.add_header('Content-ID', '<0>')
#     mime.add_header('X-Attachment-Id', '0')
#     # 把附件的内容读进来
#     mime.set_payload(f.read())
#     # 用Base64编码
#     encoders.encode_base64(mime)
#     # 添加到MIMEMultipart:
#     msg.attach(mime)
# server = smtplib.SMTP(smtp_server, 25)
server = smtplib.SMTP(smtp_server, 587) # Gmail端口,安全连接
# 安全连接调用starttls()
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/3/29 11:52
# @Author   : tangky
# @Site     : 
# @File     : handlers.py
# @Software : PyCharm

"""
编写MVC
Model-View-Controller
"""
import re
import time
import json
import hashlib
import base64
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

import markdown
from aiohttp import web

from apis import Page, APIResourceNotFoundError, APIValueError, APIPermissionError
from models import User, Comment, Blog, next_id
from coroweb import get, post
from config import configs

"""

@get('/')
async def index(request):
    users = await User.findAll()
    logging.info(users)
    return {
        '__template__': 'test.html',
        'users': users,
    }
后端API:
获取日志:GET /api/blogs
创建日志:POST /api/blogs
修改日志:POST /api/blogs/:blog_id
删除日志:POST /api/blogs/:blog_id/delete
获取评论:GET /api/comments
创建评论:POST /api/comments
修改评论:POST /api/comments/:comment_id
删除评论:POST /api/comments/:comment_id/delete
创建新用户:POST /api/users
获取用户:GET /api/users

管理页面包括:
评论列表页:GET /manage/comments
日志列表页:GET /manage/blogs
创建日志页:POST /manage/blogs/create
修改日志页:POST /manage/blogs
用户列表页:GET /manage/users

用户浏览页包括:
注册页:GET /register
登录页:GET /signin
注销页:GET /signout
首页:GET /
日志详情页:GET /blog/:blog_id
"""

COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret


# 查看是否是管理员用户
def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()


# 获取页码信息
def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


# 计算加密cookie
def user2cookie(user, max_age):
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


# 文本转HTML
def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
                filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)


# 解密cookie
async def cookie2user(cookie_str):
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


# 处理首页URL
@get('/')
async def index(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        blogs = []
    else:
        blogs = await Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return {
        '__template__': 'blogs.html',
        'page': p,
        'blogs': blogs,
    }


# 处理日志详情页URL
@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = markdown.markdown(c.content)
    blog.html_content = markdown.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments,
    }
# 处理注册页面URL
@get('/register')
def register():
    return {
        '__template__': 'register.html',
    }
# 处理登录页面URL
@get('/signin')
def signin():
    return {
        '__template__': 'signin.html',
    }
# 用户登录验证API
@post('/api/authenticate')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r
# 用户注销
@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-delete-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r
# 获取管理页面
@get('/manage')
def manage():
    return  'redirect:/manage/comments'
# 评论管理页面
@get('/manage/comments')
def manage_comments(*, page='1'):
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page),
    }
# 日志管理页面
@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page),
    }
# 创建日志页面
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs',
    }
# 编辑日志页面

# 用户管理页面
# 获取评论信息API
# 用户发表评论API
# 管理员删除评论API
# 获取用户信息API
# 定义EMAIL和HASH的格式规范
# 用户注册API
# 获取日志列表API
# 获取日志详情API
# 发表日志API
# 编辑日志API
# 删除日志API
# 删除用户API

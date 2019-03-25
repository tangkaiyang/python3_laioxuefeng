#  -*- coding:UTF-8 -*-

# from turtle import *
#
# # 设置色彩模式是RGB
# colormode(255)
#
# lt(90)
#
# lv = 14
# l = 120
# s = 45
#
# width(lv)
#
# # 初始化RGB颜色
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)
#
# penup()
# bk(l)
# pendown()
# fd(l)
#
# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()
#
#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color.
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)
#
#     l = 3.0 / 4.0*l
#     lt(s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)
#
#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)
#
#     # restore the previous pen width
#     width(w)
#
# speed("fastest")
# draw_tree(l, 4)
# done()


# import turtle
# import random
# from turtle import *
# from time import sleep
#
# t = turtle.Turtle()
# w = turtle.Screen()
#
#
# def tree(branchLen, t):
#     if branchLen > 3:
#         if 8 <= branchLen <= 12:
#             if random.randint(0, 2) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 3)
#         elif branchLen < 8:
#             if random.randint(0, 1) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 2)
#         else:
#             t.color('sienna')
#             t.pensize(branchLen / 10)
#
#         t.forward(branchLen)
#         a = 1.5 * random.random()
#         t.right(20*a)
#         b = 1.5 * random.random()
#         tree(branchLen-10*b, t)
#         t.left(40*a)
#         tree(branchLen-10*b, t)
#         t.right(20*a)
#         t.up()
#         t.backward(branchLen)
#         t.down()
#
#
# def petal(m, t):  # 树下花瓣
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         t.color("lightcoral")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)
#
#
# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     getscreen().tracer(5, 0)
#     turtle.screensize(bg='wheat')
#     t.left(90)
#     t.up()
#     t.backward(150)
#     t.down()
#     t.color('sienna')
#     tree(60, t)
#     petal(100, t)
#
#     myWin.exitonclick()
#
#
# main()


# from turtle import *
# from random import *
# from math import *
#
# def tree(n, l):
#     pd() # 下笔
#     # 阴影效果
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 3)
#     forward(l) # 画树枝
#
#
#     if n > 0:
#         b = random() * 15 + 10 # 右分支偏转角度
#         c = random() * 15 + 10 # 左分支偏转角度
#         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
#         # 右转一定角度，画右分支
#         right(b)
#         tree(n - 1, d)
#         # 左转一定角度，画左分支
#         left(b + c)
#         tree(n - 1, d)
#
#         # 转回来
#         right(c)
#     else:
#         # 画叶子
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n*0.8, n*0.8)
#         circle(3)
#         left(90)
#
#         # 添加0.3倍的飘落叶子
#         if(random() > 0.7):
#             pu()
#             # 飘落
#             t = heading()
#             an = -40 + random()*40
#             setheading(an)
#             dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
#             forward(dis)
#             setheading(t)
#
#
#             # 画叶子
#             pd()
#             right(90)
#             n = cos(radians(heading() - 45)) / 4 + 0.5
#             pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
#             circle(2)
#             left(90)
#             pu()
#
#             #返回
#             t = heading()
#             setheading(an)
#             backward(dis)
#             setheading(t)
#
#     pu()
#     backward(l)# 退回
#
# bgcolor(0.5, 0.5, 0.5) # 背景色
# ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
# tracer(0, 0)
# pu() # 抬笔
# backward(100)
# left(90) # 左转90度
# pu() # 抬笔
# backward(300) # 后退300
# tree(12, 100) # 递归7层
# done()

from turtle import *
from random import *
from math import *

def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)

bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(13, 100)
done()
# -*- coding:UTF-8 -*-

"""
事件(Event类)
Python线程的事件用于主线程控制其他线程的执行,事件是一个简单的线程同步对象,其主要提供以下方法:
方法          注释
clear           将flag设置为"False"
set             将flag设置为"True"
is_set          判断是否设置了flag
wait            会一直监听flag,如果没有检测flag就一致处于阻塞状态
事件处理的机制:全局定义一个"Flag",当flag值为False,那么event.wait()就会阻塞,当flag为True,那么event.wait()便不再阻塞
"""
# 利用Event类模拟红绿灯
import threading
import time


event = threading.Event()

def lighter():
    count = 0
    event.set()     # 初始为绿灯
    while True:
        if 5 < count <= 10:
            event.clear()   # 红灯,清除标志位
            print("\33[41;1mred light is on...\033[0m")
        elif count > 10:
            event.set()     # 绿灯,设置标志位
            count = 0
        else:
            print("\33[42;1mgreen light is on...\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():      # 判断是否设置了标志位
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light, waiting..." % name)
            event.wait()
            print("[%s] green light is on , start going..." % name)

light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car, args=("MINI", ))
car.start()
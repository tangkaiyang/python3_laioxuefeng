# -*- coding:utf-8 -*-
"""
在Linux中,每个进程都是由父进程提供的.每启动一个子进程就从父进程克隆一份数据,但是进程之间的数据本身是不能共享的
"""
# from multiprocessing import Process
# import time
#
# def f(name):
#     time.sleep(2)
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob', ))
#     p.start()
#     p.join()

from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getpid())   # 获取父进程id
    print('process id:', os.getpid())       # 获取自己的进程id
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob', ))
    p.start()
    p.join()
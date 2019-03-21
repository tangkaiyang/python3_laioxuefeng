# -*- coding:UTF-8 -*-
"""
通过Manager可实现进程间数据的共享.Manager()放回的manager对象会通过一个服务进程,来使其他进程通过代理的方式操作Python对象.
manager对象支持 list, dict, Namespace, Lock, Rlock, Semaphore, BounderSemaphore, Condition, Event, Barrier, Queue, Value
, Array
"""
from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()

        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)
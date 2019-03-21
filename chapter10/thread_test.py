# -*- coding:utf-8 -*-
import threading, time

# 新线程执行的代码
# def loop():
#     print("thread %s is running..." % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# # t = threading.Thread(target=loop, name='LoopThread')
# t = threading.Thread(target=loop)
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# 多个线程同时操作一个变量引发混乱
# 假定这是你的银行存款
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取,结果应该为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        #先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完了一定要释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) # 因为print()执行时间太长,导致冲突的概率降了99%?,性能测试的时候避免print


# total = 0
#
#
# def add():
#     # 1.dosomething1
#     # 2.io操作
#     # 1.dosomething3
#     global total
#     for i in range(1000000):
#         total += 1
#
#
# def desc():
#     global total
#     for i in range(1000000):
#         total -= 1
#
#
# import threading
#
# thread1 = threading.Thread(target=add)
# thread2 = threading.Thread(target=desc)
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(total)
# -*- coding:UTF-8 -*-

# import threading
#
# # 创建全局ThreadLocal对象
# local_school = threading.local()
#
# def process_student():
#     # 获取当前线程关联的student
#     # std = local_school.student
#     print('Hello, %s (in %s)' % (local_school.student, threading.current_thread().name))
#
# def process_thread(name):
#     # 绑定ThreadLocal的student
#     local_school.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import threading
# global_num = 0
# lock = threading.Lock()
# def thread_cal():
#     global global_num
#     for i in range(1000):
#         lock.acquire()
#         global_num += 1
#         lock.release()
#
# # Get 10 threads , run them and wait them all finished.
# threads = []
# for i in range(10):
#     threads.append(threading.Thread(target=thread_cal))
#     threads[i].start()
# for i in range(10):
#     threads[i].join()
#
# # Value of global variable can be confused.
# print(global_num)

# import threading
#
# def show(num):
#     print(threading.current_thread().getName(), num)
#
# def thread_cal():
#     local_num = 0
#     for _ in range(1000):       # '_'代表最后一个计算结果
#         local_num += 1
#     show(local_num)
#
# threads = []
# for i in range(10):
#     threads.append(threading.Thread(target=thread_cal))
#     threads[i].start()

# import threading
#
# global_data = threading.local()
#
# def show():
#     print(threading.current_thread().name, global_data.num)
#
# def thread_cal():
#     global_data.num = 0
#     for i in range(1000):
#         global_data.num += 1
#     show()
#
# threads = []
# for i in range(10):
#     threads.append(threading.Thread(target=thread_cal))
#     threads[i].start()
#
#
# print("Main thread", global_data.__dict__)

# import threading
# import time
#
# def run(n):
#     print('task', n, threading.current_thread())        # 输出当前的线程
#     time.sleep(1)
#     print('3s')
#     time.sleep(1)
#     print('2s')
#     time.sleep(1)
#     print('1s')
#
# start_time = time.time()
#
# t_obj = []                                  # 定义列表用于存放子线程实例
#
# for i in range(3):
#     t = threading.Thread(target=run, args=("t-%s" % i,))
#     t.start()
#     t_obj.append(t)
#
# """
# 有主线程生成的三个子线程
# ..
# """
#
# for tmp in t_obj:
#     t.join()                            # 为每个子线程添加join后,主线程就会等这些子线程执行完毕后在执行
# print("cost:" , time.time() - start_time) # 主线程
# print(threading.current_thread())       # 输出当前线程

"""
信号量(BoundedSemaphore类)
互斥锁同时只允许一个线程更改数据,而Semaphore是同时允许一定数量的线程更改数据
"""
import threading
import time

num = 0
semaphore = threading.BoundedSemaphore(5) # 最多允许5个线程同时运行
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread:%s\n" % n)
    semaphore.release()


for i in range(22):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()

while threading.active_count() != 1:
    pass
else:
    print('----------all threads done-----------')
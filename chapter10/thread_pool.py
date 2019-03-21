# -*- coding:UTF-8 -*-

"""
进程池
由于进程启动的开销比较大,使用多进程的时候会导致大量内存空间被消耗.为了防止这种情况发生可以使用进程池,(由于启动线程的开销比较小,
所以不需要线程池这种概念,多线程只会频繁地切换cpu导致系统变慢,并不会占用过多的内存空间)
进程池中常用方法:
apply()     同步执行(串行)
apply_async()   异步执行(并行)
terminate()     立刻关闭进程池
join()          主进程等待所以子进程执行完毕.必须在close或terminate()之后
close()         等待所有进程结束后,才关闭进程池

进程池内部维护一个进程序列,当使用时,去进程池中获取一个进程,如果进程池序列中没有可供使用的进程,那么程序就会等待,直到进程池中
有可用进程为止.在上面的程序中产生了10个进程,但是只能由5个被放入进程池,剩下的都被暂时挂起,并不占用内存空间,等前面的五个进程执行
完成后,再执行剩下5个进程
"""
from multiprocessing import Process, Pool
import time

def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print('-->exec done:', arg)

pool = Pool(5)  # 允许进程池同时放入5个进程

for i in range(5):
    pool.apply_async(func=Foo, args=(i, ), callback=Bar)    # func子进程执行完后,才会执行callback,否则callback不执行(而且callback是由父进程来执行的)
    pool.apply(func=Foo, args=(i, ))

print('end')
pool.close()
pool.join() # 主进程等待所有子进程执行完毕.必须在close()或terminate()之后
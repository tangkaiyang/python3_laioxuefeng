#  如果要启动大量的子进程,还可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)... ' % (name, os.getpid()))
    start_time = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start_time)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocess done...')
    p.close()  # 调用join()之前先调用close(),不能继续添加新的Process
    p.join()  # 等待所有子进程执行完毕
    print('All subprocess done.')

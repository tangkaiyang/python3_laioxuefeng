#  -*- coding:UTF-8 -*-

# import asyncio


# @asyncio.coroutine
# async def hello():
#     print('Hello world!')
#     # 异步调用asyncio.sleep(1)
#     # r = yield from asyncio.sleep(1)
#     await asyncio.sleep(1)
#     print('Hello again!')
#
#
# # 获得Eventloop
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()
"""
@asyncio.coroutine把一个generator标记为coroutine类型,然后,我们就把这个coroutine扔到Eventlop中执行.
hello()会首先打印出Hello world!,然后,yield from语法可以让我们方便地调用另一个generator.
由于asyncio.sleep()也是一个coroutine,所以线程不会等待asyncio.sleep(),而是直接终端并执行下一个消息循环.
当asyncio.sleep()返回时,线程就可以从yield from拿到返回值(此处是None),然后接着执行下一行语句.
把asyncio.sleep(1)看成是一个耗时1秒的IO操作,在此期间,主线程并未等待,而是去执行EventLoop中其他可以执行的coroutine了,
因此可以实现并发执行
"""

# 用Task封装两个coroutine

import asyncio
import threading


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
由打印的当前线程名可以看出,两个coroutine是由同一个线程并发执行的.
如果把asyncio.sleep()换成真正的IO操作,则多个coroutine就可以由一个线程并发执行.
"""

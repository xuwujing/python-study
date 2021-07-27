# Exectuor 提供了如下常用方法：
# submit(fn, *args, **kwargs)：将 fn 函数提交给线程池。*args 代表传给 fn 函数的参数，*kwargs 代表以关键字参数的形式为 fn 函数传入参数。
# map(func, *iterables, timeout=None, chunksize=1)：该函数类似于全局函数 map(func, *iterables)，
# 只是该函数将会启动多个线程，以异步方式立即对 iterables 执行 map 处理。
# shutdown(wait=True)：关闭线程池。
# Future 提供了如下方法：
# cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
# cancelled()：返回 Future 代表的线程任务是否被成功取消。
# running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
# done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
# result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
# exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
# add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。

from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum
# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)
# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 5)
# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 10)
# 判断future1代表的任务是否结束
print(future1.done())
time.sleep(3)
# 判断future2代表的任务是否结束
print(future2.done())
# 查看future1代表的任务返回的结果
print(future1.result())
# 查看future2代表的任务返回的结果
print(future2.result())
# 关闭线程池
pool.shutdown()




# 定义一个准备作为线程任务的函数
def action2(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum
# 创建一个包含2条线程的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    # 向线程池提交一个task, 50会作为action()函数的参数
    future1 = pool.submit(action2, 5)
    # 向线程池再提交一个task, 100会作为action()函数的参数
    future2 = pool.submit(action2, 10)
    def get_result(future):
        print(future.result())
    # 为future1添加线程完成的回调函数
    future1.add_done_callback(get_result)
    # 为future2添加线程完成的回调函数
    future2.add_done_callback(get_result)
    print('--------------')



# 定义一个准备作为线程任务的函数
def action3(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum
# 创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(action3, (5, 10, 15))
    print('--------------')
    for r in results:
        print(r)
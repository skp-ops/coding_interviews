'''

进程池
    如果在开发过程中无限制地创建进程，或者创建线程，都可能会导致程序效率降低
    进程池就很好地解决了创建多个进程的操作

'''
# 如何实现进程池
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # 进程池和线程池导入

def task(a):
    print(a,end=' ')
    time.sleep(0.5)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)

# 0 1 2 3 4 5 6 7 8 9

#################################################
pool.shutdown(True) # 我希望进程池里的进程全部完成操作命令之后再进行之后的操作，就用shutdown命令
                    # 比较类似进程的join方法

import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # 进程池和线程池导入

def task(a):
    print(a,end=' ')
    time.sleep(0.5)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)
    pool.shutdown(True)
    time.sleep(1)
    print('over')

# 0 1 2 3 4 5 6 7 8 9 over

#################################################
# 进程也可以跟线程一样进行回调
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # 进程池和线程池导入

def task(a):
    print(a,end=' ')
    time.sleep(0.5)
    return a

def other_task(res):
    time.sleep(1)
    print('回调',res.result())
    print('当前进程id', multiprocessing.current_process().pid)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        fur = pool.submit(task, i)
        fur.add_done_callback(other_task) # 这个other_task 是由主进程去完成的
                                          # 在线程池中，回调函数都是由子线程完成的

    pool.shutdown(True)
    print('over')
# 0 1 2 3 4 回调 0
# 当前进程id 10572
# 5 6 7 8 9 回调 2
# 当前进程id 10572
# 回调 1
# 当前进程id 10572
# 回调 3
# 当前进程id 10572
# 回调 4
# 当前进程id 10572
# 回调 5
# 当前进程id 10572
# 回调 8
# 当前进程id 10572
# 回调 7
# 当前进程id 10572
# 回调 6
# 当前进程id 10572
# 回调 9
# 当前进程id 10572
# over

#################################################
# 在线程池加锁的时候不能直接加，需要基于Manager中的Lock和RLock来实现
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # 进程池和线程池导入

def task(a,lock):
    with lock:
        print(a,end=' ')
        time.sleep(0.5)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # lock = multiprocessing.Lock() 这个锁不能使用
    manager = multiprocessing.Manager()
    lock = manager.RLock()
    for i in range(10):
        pool.submit(task, i, lock,)
    pool.shutdown(True)
    print('over')
# 0 1 2 3 4 5 6 7 8 9 over

#################################################
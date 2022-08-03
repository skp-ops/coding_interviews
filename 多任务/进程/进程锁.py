'''

进程锁：
    当程序多个进程抢占式去做某些操作的时候，（抢占某些资源时）为了防止操作出问题，可以通过进程锁来避免

'''
# 如果没有进程锁，出现的问题如下：
import time
import multiprocessing
from multiprocessing import Value

def func(a):
    a.value  += 1

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    v = Value('i', 0)
    for i in range(1000):
        p = multiprocessing.Process(target=func, args=(v,))
        p.start()

    time.sleep(3)
    print(v.value)
    # 996,不是1000，说明多个子进程抢资源了


# 加了锁之后就显示1000了
import time
import multiprocessing
from multiprocessing import Value

def func(a, lock):
    lock.acquire()
    a.value += 1
    lock.release()

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    v = Value('i', 0)
    lock = multiprocessing.RLock() # 进程锁
    for i in range(1000):
        p = multiprocessing.Process(target=func, args=(v,lock))
        p.start()

    time.sleep(3)
    print(v.value)
    # 1000
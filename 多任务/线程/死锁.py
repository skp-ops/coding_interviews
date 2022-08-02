'''

死锁：
    由于竞争资源或者由于彼此通信而造成的一种阻塞的现象

'''
# 死锁程序
##########################################################
# eg1
import threading

num = 0

lock = threading.Lock()

def task():
    lock.acquire() # 申请锁
    lock.acquire()  # 这里申请了两边Lock，程序锁死了
    global num
    for i in range(1000000):
        num += 1
    print(num)
    lock.release() # 释放锁
    lock.release()  # 释放锁

for i in range(2):
    t = threading.Thread(target=task)
    t.start()
##########################################################

##########################################################
# eg2
'''
两个线程各自拿着一把锁，都在等待对方释放锁
这样会导致两个线程一直无法释放锁
'''
import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def task_1():
    lock_1.acquire()
    time.sleep(1)
    lock_2.acquire()
    print(1)
    lock_2.release()
    print(2)
    lock_1.release()
    print(3)

def task_2():
    lock_2.acquire()
    time.sleep(1)
    lock_1.acquire()
    print(1)
    lock_1.release()
    print(2)
    lock_2.release()
    print(3)

t1 = threading.Thread(target=task_1)
t1.start()

t2 = threading.Thread(target=task_2)
t2.start()
##########################################################
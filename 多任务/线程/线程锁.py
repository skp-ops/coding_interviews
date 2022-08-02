'''

线程锁：
    在程序中如果想要自己手动加锁，一般有两种：Lock和RLock

'''
'''
Lock, 同步锁
Lock不支持锁的嵌套
即
不能
    lock acquire():
    lock acquire(): 这样就进入了死锁状态
    
但是
可以
    lock acquir():
    lock release():
    lock acquir():
    lock release():
'''
#############################################
import threading

num = 0

lock = threading.Lock()

def task():
    lock.acquire() # 申请锁
    global num
    for i in range(1000000):
        num += 1
    print(num)
    lock.release() # 释放锁

for i in range(2):
    t = threading.Thread(target=task)
    t.start()
#############################################
'''
RLock, 递归锁
RLock支持锁的嵌套
'''
#############################################
import threading

num = 0

lock = threading.RLock()

def task():
    lock.acquire() # 申请锁
    global num
    for i in range(1000000):
        num += 1
    print(num)
    lock.release() # 释放锁

for i in range(2):
    t = threading.Thread(target=task)
    t.start()
#############################################
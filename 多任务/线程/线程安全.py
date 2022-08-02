'''

线程安全：
    一个进程中可以有多个线程，且线程共享所有进程中的资源
    多个线程同时去操作一个“东西”的时候，可能会存在数据紊乱的情况
    我们就必须要避免这样的情况

'''
# 数据紊乱的例子
##########################################################
# eg1
import threading

loop = 1000000000
number = 0

def sum(num):
    global number
    for i in range(num):
        number += 1

def sub(num):
    global number
    for i in range(num):
        number -= 1

t_sum = threading.Thread(target=sum, args=(loop,))
t_sub = threading.Thread(target=sub, args=(loop,))
t_sum.start()
t_sub.start()

t_sum.join()
t_sub.join()

print(number)
##########################################################
# eg2
import threading
num = 0
def task():
    global num
    for i in range(1000000):
        num += 1
    print(num)
for i in range(2):
    t = threading.Thread(target=task)
    t.start()
    # 1563212 # 并不是加到100000
    # 2000000

##########################################################

# 如何去避免这种情况，需要给每个任务进行加锁操作
# 如果一个线程在执行某一个任务的时候进行了申请锁的操作
# 谁是第一个到来的，那么就申请到了这把锁，该线程继续向下执行
# 其他没有申请到的锁原地等待，直到该锁被解开，这个线程才能申请到锁
# 必须要用同一把锁，这样两个线程在申请的时候则会使用同一把锁

##########################################################
# eg1
import threading

lock = threading.RLock() # 定义一个锁参数lock

loop = 1000000000
number = 0

def sum(num):
    lock.acquire() # 申请加锁
    global number
    for i in range(num):
        number += 1
    lock.release() # 解锁、释放锁

def sub(num):
    lock.acquire() # 申请加锁
    global number
    for i in range(num):
        number -= 1
    lock.release() # 解锁、释放锁

t_sum = threading.Thread(target=sum, args=(loop,))
t_sub = threading.Thread(target=sub, args=(loop,))
t_sum.start()
t_sub.start()

t_sum.join()
t_sub.join()

print(number)
##########################################################

# eg2
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
    # 1000000
    # 2000000 运行正常

##########################################################

import threading

num = 0

lock = threading.RLock()

def task():
    with lock: #自动加锁 基于上下文管理，内部自动运行 acquire 和 release
        global num
        for i in range(1000000):
            num += 1
    print(num)

for i in range(2):
    t = threading.Thread(target=task)
    t.start()
    # 1000000
    # 2000000 运行正常
##########################################################

'''
线程安全的操作有哪些：
1. L.append(x)
2. L1.extend(L2)
3. x = L[i]
4. x = L.pop()
5. L1[i:j] = L2
6. L.sort()

7. x = y
8. x.field = y

9. D[x] = y
10. D1.update(D2)
11. D.keys()

'''
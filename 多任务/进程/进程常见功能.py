'''

进程常见功能

'''
import multiprocessing
def task():
    pass

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.start()

# 相关功能有如下：
########################################################

p1.start() # 当前进程准备就绪，等待CPU调度（工作单元其实是进程中的主线程）

########################################################

p1.join() # 等待当前进程的任务执行完毕后再向下继续执行

########################################################
import multiprocessing
import time
def task():
    time.sleep(2)
    print('当前是子进程在运行')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.start()
    p1.join()

    print('当前是主进程在运行')
# 当前是子进程在运行
# 当前是主进程在运行
########################################################

p1.daemon=bool # 守护进程，必须放在start之前
    # True 表示设置为守护进程，主进程执行完毕后，子进程也自动关闭
    # False 表示设置为非守护进程，主进程等待子进程，子进程执行完毕后，主进程才结束，默认为False

########################################################
import multiprocessing
import time
def task():
    time.sleep(2)
    print('执行中......')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.daemon = True
    p1.start()
    print('运行结束')
# 运行结束，不会等待子进程打印，主进程执行结束直接整体结束
########################################################

p1.name = 'xxx' # 进程的名称的设置和获取

########################################################
import multiprocessing
import time
def task():
    time.sleep(0.2)
    print('当前子进程的名称为',multiprocessing.current_process().name)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.name = 'ABC'
    p1.start()

    print('a')
# a
# 当前子进程的名称为 ABC

########################################################

# 获取子进程、父进程id，获取进程中线程的个数

########################################################
import os
import time
import threading
import multiprocessing

def func():
    time.sleep(0.5)

def task():
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()
    print('当前线程的个数为', len(threading.enumerate()), '分别是', threading.enumerate())
    print('当前子进程id为', os.getpid(),'当前父进程id为',os.getppid())
    time.sleep(0.2)
    print('当前子进程的名称为', multiprocessing.current_process().name)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.name = 'ABC'
    p1.start()

# 当前线程的个数为 11 分别是 [<_MainThread(MainThread, started 16524)>,
#                         <Thread(Thread-1 (func), started 14996)>,
#                         <Thread(Thread-2 (func), started 7124)>,
#                         <Thread(Thread-3 (func), started 16452)>,
#                         <Thread(Thread-4 (func), started 2128)>,
#                         <Thread(Thread-5 (func), started 6292)>,
#                         <Thread(Thread-6 (func), started 1740)>,
#                         <Thread(Thread-7 (func), started 5548)>,
#                         <Thread(Thread-8 (func), started 13648)>,
#                         <Thread(Thread-9 (func), started 17324)>,
#                         <Thread(Thread-10 (func), started 8272)>]
# 当前子进程id为 15164 当前父进程id为 13560
# 当前子进程的名称为 ABC

########################################################

# 自定义进程类，直接将线程需要做的事情写到run方法中

########################################################
import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print('执行此进程',self._args)

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    p = MyProcess(args=('xxx',))
    p.start()
    print('继续执行...')

########################################################

# CPU个数，程序一般创建多个进程（CPU多核优势）
########################################################
import multiprocessing
a = multiprocessing.cpu_count()
print(a)
# 12 # 6核虚拟出12核
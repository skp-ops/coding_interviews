'''

进程开发与进程模式

多进程开发：
    进程是计算机中资源分配的最小单元；一个进程中可以有多个线程，同一个进程中的线程共享资源；
    但是进程与进程之间则是相互隔离的
    python中通过多进程可以利用CPU的多核优势，计算密集型操作适用于多进程

'''
# 进程介绍
import multiprocessing

def task():
    pass

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task)
    p1.start()

'''
基于multiprocessing的三种操作
fork, spawn, forkserver
'''
#################################################################
# fork，在Windows中不支持这个模式，‘拷贝’几乎所有资源，支持文件对象、线程锁等传参
#################################################################
# fork模式：
# 在主进程中改变了模式为fork，并且创建了一个名为name的空数组
# 然后再创建了一个子进程p1，由子进程运行task函数
import multiprocessing

def task():
    print(name)

if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []

    p1 = multiprocessing.Process(target=task) # windows系统不支持fork，无法改成fork模式
    p1.start()
# 输出[],在子进程中能找到这个name，但是子进程中的name和主进程中的name是两份数据
# 各自在各自的进程中维护数据

# 下面这个示例就很好的展示了上述的特性，在子进程中操作的对象和主进程中操作的对象并不是同一个
# 所以子进程将123append到了name中，不会同步到主进程，主进程仍然是空数组
import multiprocessing
import time

def task():
    print(name)
    name.append(123)
if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    name = []

    p1 = multiprocessing.Process(target=task) # windows系统不支持fork，无法改成fork模式
    p1.start()

    time.sleep(2)
    print(name)
# 子进程在name里加了123，但是主进程在sleep等了2秒，子进程里的name改变了，但是主进程的name仍然是空数组
# 所以打印的都是 [] []

#################################################################
# spawn，run参数传必备资源，不支持文件对象、线程锁等传参
#################################################################
# spawn，不会主动去拷贝一些参数，需要手动去传递一些参数
import multiprocessing
import time

def task(a):
    print(a)
    a.append(123)

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")
    name = []

    p1 = multiprocessing.Process(target=task,args=(name,))
    p1.start()

    time.sleep(2)
    print(name)

# 将主进程中的参数name交给了子进程，需要人为去添加这个参数，而不是自动拷贝
# 但是跟fork一样，子进程和主进程用的仍然是两份数据，各自维护各自的数据
# 打印的结果仍然是[] []

#################################################################
# forkserver，run参数传必备资源，不支持文件对象、线程锁等传参，支持部分unix系统
#################################################################
# 在程序刚运行的时候,创建一个模板,这个模板相当于什么都没有的进程,没有维护任何值
# 如果再去创建进程,就把这个模板拷贝一遍,拷贝的内容里没有任何值
# 同样需要人为传递参数去执行其他命令
import multiprocessing
import time

def task(a):
    print(a)
    a.append(123)

if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")
    name = []

    p1 = multiprocessing.Process(target=task,args=(name,))
    p1.start()

    time.sleep(2)
    print(name)
#################################################################
'''

并发编程：
    提升代码执行的效率
    假如原来的代码执行起来需要几十分钟，并发编程可以在一分钟执行完毕

'''

'''
并发编程包含：线程、进程、协程
在之后的目录当中，包含了相关核心知识的解释，以及利用python进行并发编程
'''

'''
首先什么是线程和进程，有两个比较容易理解的例子
    一个工厂，至少有一个车间，而一个车间至少有一个工人，这个工人在工作
    为了提高产能，可以增加多个车间，或者一个车间里增加多个工人
或者是
    一个火车站，至少有一列动车，一列动车有至少一节车厢，这个车厢是最小的火车站单元

这里就可以将工厂、火车站比作程序
    车间、动车比作进程
    工人、车厢比作线程
    
在python中实现起来就是，使用python执行了一个文件 xx.py运行时，内部就创建了一个进程（主进程），在进程中创建了一个线程（主线程）
由线程逐行运行代码

线程：是计算机中可以被cpu调度的最小单元（真正工作的单位）
进程：是计算机资源分配的最小单元（进程为线程提供资源）

一个进程中可以有多个线程，同一个进程中的线程可以共享此进程中的资源
'''

#################################################################
# 线程
import threading # 导入的这个模块用来创建多个线程

def task(a,b,c,d):
    print(a)
    print(b,end=' ')
    print(c)
    print(d)
    return None

# 创建一个线程t来完成任务函数task，同时如果函数有参数则将参数传入
t = threading.Thread(target=task, args=('cat','dog','fish','abc'))
# 线程工作
t.start()

print('这串字符表示，线程在执行任务的时候，不会等待所有任务执行完再执行之后的任务，'
      '而是在线程启动的一瞬间就向下继续执行任务')

#################################################################
# 如何创建多个线程
import threading

task_list = {
    'sum': 100000,
    'multi': 5,
    'print': '多线程操作任务3，打印任务'
}

def work(fun_name, value):
    temp = 1
    if fun_name == 'sum':
        for i in range(value):
            temp += 1
        print(temp)
    elif fun_name == 'multi':
        for i in range(1, value+1):
            temp *= i
        print(temp)
    elif fun_name == 'print':
        print(value)
    return None
if __name__ == '__main__':
    for name, value in task_list.items(): # 三个任务同步执行, 而且这个for循环不会在此等待，而是立刻向下执行其他任务
        t = threading.Thread(target=work, args=(name,value))
        t.start()

#################################################################
# 多进程
import multiprocessing # 导入多进程
import time

def mptask(a1,a2,a3):
    temp = 0
    for i in range(a1):
        for j in range(a2):
            for k in range(a3):
                temp += 1
    print(f'输出结果为{temp}',end= '')
    print('结束任务时间为：',end=' ')
    print(time.time())
    return

value = [
    (10,20,30),
    (5,90,3),
    (12,35,2)
]
if __name__ == '__main__':
    print('开始时间：',end=' ')
    print(time.time())
    for a1, a2, a3 in value:
        t = multiprocessing.Process(target=mptask, args=(a1,a2,a3))
        # 进程创建后，在进程中还会创建一个线程
        t.start()
'''
开始时间： 1659421936.9624095
输出结果为1350结束任务时间为： 1659421937.0212522
输出结果为6000结束任务时间为： 1659421937.0212522
输出结果为840结束任务时间为： 1659421937.0222495
'''
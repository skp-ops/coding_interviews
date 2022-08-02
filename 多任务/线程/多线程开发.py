'''

多线程开发

'''
import threading

def task(arg):
    pass

# 创建一个Thread对象（对象），并封装线程被CPU调度时应执行的任务和相关参数。
t = threading.Thread(target=task, args=arg)
# 线程准备就绪（等待CPU调度），代码继续向下执行
t.start()

print('继续执行之后的操作') # 主线程执行所有代码，不结束，等待子线程

'''
线程的方法：
'''

t.start() # 当前线程准备就绪（等待CPU调度，具体时间有CPU来决定）
    '''
    import threading

    loop = 1000000
    number = 0
    
    def _add(count):
        global number
        for i in range(count):
            number += 1
    
    t = threading.Thread(target=_add, args=(loop,))
    t.start()
    
    print(number) 
    # 223585,打印的数并不是1000000000，说明主线程不会等待子线程，继续向下运行，直到子线程也运行完毕才结束整个代码
    '''

t.join() # 等待当前线程的任务执行完毕后再向下继续执行
    # 如果两个线程并行运行，去处理同一个数据，就会导致程序在运行，两个线程切片运行的时候
    # 数据在A线程是x，数据还没转变为y的时候，就被B线程拿去用，这个时候等待A线程的数据处理完数据已经发生改变了
    # 但是在B线程中数据还是原来的X，会造成数据紊乱，所以需要join特性
    '''
    import threading
    
    number = 0
    
    def _add():
        global number
        for i in range(10000000):
            number += 1
    
    t = threading.Thread(target=_add)
    t.start()
    
    t.join() # 主线程等待中...
    print(number) # 10000000 打印的是10000000，说明子线程执行完了再向后执行这个print命令

    '''

t.setDaemon(True(or False)) # 守护线程（必须放在start之前）  python 3.0 弃用
    t.setDaemon(True) # 设置为守护线程，主线程执行完毕后，子线程也自动关闭
    t.setDaemon(False) # 设置为非守护线程，主线程等待子线程，子线程执行完毕后，主线程才结束。（默认）
    '''
    import threading
    import time
    
    def task():
        time.sleep(5)
        print('Over')
    
    t = threading.Thread(target=task)
    t.setDaemon(True) #python 3.0 弃用
    t.start()
    
    print('END')
    '''

t.name # 线程名称的设置和获取
    '''
    import threading
    import time
    
    def task():
        name = threading.current_thread().name
        print(name)
    
    for i in range(10):
        t = threading.Thread(target=task)
        t.name = f'线程名称{i}' # 需要在start之前
        t.start()
    # 线程名称0
    # 线程名称1
    # 线程名称2
    # 线程名称3
    # 线程名称4
    # 线程名称5
    # 线程名称6
    # 线程名称7
    # 线程名称8
    # 线程名称9
    '''

# 自定义一个类来创建线程
    '''
    import threading
    class MyThread(threading.Thread): # 继承原来的线程类threading.Thread
        def run(self): # 线程具体要执行的事
            print('执行此线程', self._args)
    
    t = MyThread(args=100)
    t.start()
    '''
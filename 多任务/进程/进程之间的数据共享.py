'''

进程之间的数据共享
    进程是资源分配的最小单元，每个进程中都维护自己独立的数据，不共享

'''
###############################################################
# 共享内存
# 数据可以存储在共享内存的容器里，这样再被子进程调用的时候就能实时更改内容
# 'c ' : ctypes.c_char,   'u ' : ctypes.c_wchar,
# 'b ' : ctypes.c_byte,   'B ' : ctypes.c_ubyte,
# 'h ' : ctypes.c_short,  'H ' : ctypes.c_ushort,
# 'i ' : ctypes.c_int,    'I ': ctypes.c_uint,      (其u表示无符号)
# 'l ' : ctypes.c_long,   'L ' : ctypes.c_ulong,
# 'f ' : ctypes.c_float,  'd ' : ctypes.c_double

from multiprocessing import Process, Value, Array

def func(a1, a2, a3):
    a1.value = 888
    a2.value = 'a'.encode('utf-8')
    a3.value = "鸡"

if __name__ == '__main__':
    num = Value('i', 123) # i表示一个整数
    a = Value('c') # c表示一个字符
    b = Value('u') # u表示一个汉字（占两个字节的字符串）

    p = Process(target=func, args=(num, a, b))
    p.start()
    p.join()

    print(num.value, a.value, b.value)
    # 888 b'a' 鸡


from multiprocessing import Process, Value, Array

def func(data_array):
    data_array[0] = 123

if __name__ == '__main__':
    arr = Array('i', [123, 123, 154, 22]) # i 表示这个数组里只能放整型，且以后不能添加删除元素
    p = Process(target=func, args=(arr,))
    p.start()
    p.join()

    print(arr[:])
    # [123, 123, 154, 22]

###############################################################
# server process ，基于manager对象，可以用列表，字典，相对灵活点
from multiprocessing import Process, Manager

def func(d, l):
    d[1] = '1'
    d['2'] = 2
    d['new_key'] = None
    l.append(123)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() # 跟普通的字典操作都是一样的
        l = manager.list() # 跟普通的列表操作都是一样的

        p = Process(target=func, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
    # {1: '1', '2': 2, 'new_key': None}
    # [123]

###############################################################
# 基于队列(先进先出) 实现交换

import multiprocessing

def func(q):
    for i in range(10):
        q.put(i)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=func, args=(queue,))
    p.start()
    p.join()

    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    # 0
    # 1
    # 2
    # 3
    # 4

###############################################################
# 基于管道（双向队列） 实现交换
import time
import multiprocessing

def func(conn):
    time.sleep(1)
    conn.send([1,2,3,4,5]) # 第三步 子进程将这个数据发送给了父进程的父管道
    data = conn.recv() #第四步 子进程发送完之后，子进程开始等待主进程发送数据过来
    print('子进程接收：', data) # 第七步
    time.sleep(2)

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe() # parent 和 child相当于管道的两端
    p = multiprocessing.Process(target=func, args=(child_conn,))
    p.start() # 第一步

    info = parent_conn.recv() # 第二步 子进程p进入func之后等待了1s钟，这个时候父进程的管道还没有接收到数据，就是阻塞状态，等待接收
    print('父进程接收：', info) #第五步 一旦父管道接收到了值，就可以执行这个命令
    parent_conn.send(123) # 第六步 父进程向子进程发送数据
# 父进程接收： [1, 2, 3, 4, 5]
# 子进程接收： 123
###############################################################
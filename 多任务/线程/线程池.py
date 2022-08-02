'''

python3 中官方正式提供线程池
    线程并不是开的越多越好，开多了可能会导致系统的性能更低

'''
'''
不建议无限制地创建线程
例如
for i in range(100000):
    t = threading.Thread(target = fun, args = (i,))
    t.start()
'''

# 建议使用线程池
# 线程池的创建和例子
##########################################################
from concurrent.futures import ThreadPoolExecutor # 将线程池导入

def task(num):
    temp = 0
    print('开始任务')
    for i in range(num**2):
        temp += 1

# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)


for i in range(50,100):
    pool.submit(task, i) # 交给线程池一个任务，让它来完成task
#     这50个任务一口气全部交给线程池了，线程池来调度
#     如果线程池中有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池，如果没有空闲线程，则等待

print('END')

##########################################################



pool.shutdown(True) # 等待线程池中的任务执行完毕后，再开始执行后续的命令
                    # 类似于线程的 t.join()



##########################################################


x = pool.submit(func1,args)
x.add_done_callback(func2) # 完成func1之后，将func1返回的参数加入到func2进行执行

from concurrent.futures import ThreadPoolExecutor # 将线程池导入

def task(num):
    temp = 0
    print('开始任务')
    for i in range(num**2):
        temp += 1
    return 1

def finish(response):
    print('task completed!', response.result())

# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)


for i in range(50,100):
    t = pool.submit(task, i) # 交给线程池一个任务，让它来完成task
#     这50个任务一口气全部交给线程池了，线程池来调度
#     如果线程池中有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池，如果没有空闲线程，则等待
    t.add_done_callback(finish) # 当t这个线程，执行完上述的pool.submit里的任务task之后，紧接着执行finish这个函数
#     相当于一个任务分工
print('END')

##########################################################

# 最终统一获取的结果
# 利用线程安全类操作例如append

from concurrent.futures import ThreadPoolExecutor # 将线程池导入
import random
def task(num):
    return random.randint(0, 999)

res = []

pool = ThreadPoolExecutor(10)


for i in range(50,100):
    t = pool.submit(task, i)
    res.append(t.result())

pool.shutdown(True)

print(res)
# [831, 125, 241, 162, 767, 3, 689, 774, 869, 697, 799, 718,
# 663, 746, 651, 747, 496, 95, 220, 831, 905, 108, 161, 771,
# 501, 517, 278, 763, 1, 397, 206, 333, 691, 242, 329, 502, 143,
# 765, 756, 238, 227, 117, 1, 49, 586, 356, 412, 424, 658, 550]

##########################################################

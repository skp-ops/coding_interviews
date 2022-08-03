import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor # 进程池和线程池导入

def task(a,lock):
    with lock:
        print(a,end=' ')
        time.sleep(0.5)

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # lock = multiprocessing.Lock() 这个锁不能使用
    manager = multiprocessing.Manager()
    lock = manager.RLock()
    for i in range(10):
        pool.submit(task, i, lock,)
    pool.shutdown(True)
    print('over')
# 0 1 2 3 4 5 6 7 8 9 over
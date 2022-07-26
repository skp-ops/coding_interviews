'''

GIL锁
global interpreter lock 全局解释器锁是Cpython解释器特有的一个东西
让一个进程中同一时刻只能有一个线程可以被CPU调用
这就导致了python线程的并发无法实现

'''

'''
如果程序想利用 计算机的“多核优势”，让CPU同时处理一些任务，适合用多进程开发（消耗的资源也会更多）
如果程序不想利用 计算机的“多核优势”，适合用多线程开发 

常见的程序开发中，计算机操作需要使用CPU的多核优势，IO操作不需要利用CPU的多核优势总结起来就是
    计算密集型，用多进程 （例如大量的数据计算【累加，累乘等】）
    IO密集型，用多线程（例如文件读写，网络数据传输等）
    
    
但是在之后的开发中，不一定需要全部使用多线程，也不一定需要全部使用多进程
可以根据任务的不同，进行不同的多线程多进程配合操作
'''
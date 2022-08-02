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
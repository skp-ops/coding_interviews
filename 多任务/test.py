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
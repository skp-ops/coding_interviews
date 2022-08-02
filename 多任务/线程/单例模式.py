'''

单例模式：
    如果通过一个类，实例化多个对象，创建多个对象时都使用同一个地址

'''
'''
错误的例子
'''
class Foo:
    pass
obj1 = Foo()
obj2 = Foo()
print(obj1, obj2)
# <__main__.Foo object at 0x0000026BD4421BA0>
# <__main__.Foo object at 0x0000026BD4421BD0> 地址不一样

'''
最传统的解决方案
'''


class singleton:
    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance
        cls.instance = object.__new__(cls)
        return cls.instance


obj_1 = singleton('abcd')
obj_2 = singleton('efgh')

print(obj_1, obj_2)
# <__main__.singleton object at 0x0000023D87663100>
# <__main__.singleton object at 0x0000023D87663100>
# 地址一样的



'''
在多线程中就会出现问题，假如多个线程进行创建实体
如果在创建的过程中，如果5个线程同时在“sleep”中等待，之后就会依次创建五个不同的对象
这样就会导致五个线程在恢复之后，继续向下执行创建新的地址不同的对象
'''
import threading
import time
class singleton:
    instance = None
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance
        time.sleep(0.5)
        cls.instance = object.__new__(cls)
        return cls.instance

def task():
    obj = singleton('aaa')
    print(obj)

for i in range(5):
    t = threading.Thread(target=task)
    t.start()
# <__main__.singleton object at 0x0000013A138F1B10>
# <__main__.singleton object at 0x0000013A138F2020>
# <__main__.singleton object at 0x0000013A138F1E10>
# <__main__.singleton object at 0x0000013A138F1FF0>
# <__main__.singleton object at 0x0000013A138F3DF0>




'''
利用多线程以及加锁来优化
加一个锁即可顺序安排线程进行操作，同时在锁之上，再增加一层判断，这样也能优化
因为假如第一次创建完对象之后，程序继续向下运行了几千行代码，这个时候又需要再来一次创建实体的操作
同样需要利用同一个地址，这个时候如果我们不加锁之上的判断，则又会加一遍锁，然后再解锁，这样就会浪费很多时间
    假如加了判断，由于之前已经划好了地址，这个时候就不用申请锁，就直接返回对象结果即可
'''

import threading
import time
class singleton:
    clock = threading.RLock()
    instance = None
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance
        time.sleep(0.5)
        with cls.clock:
            if cls.instance:
                return cls.instance
        cls.instance = object.__new__(cls)
        return cls.instance
def task():
    obj = singleton('aaa')
    print(obj)

for i in range(5):
    t = threading.Thread(target=task)
    t.start()
# <__main__.singleton object at 0x000001FC590D5000>
# <__main__.singleton object at 0x000001FC590D5000>
# <__main__.singleton object at 0x000001FC590D5000>
# <__main__.singleton object at 0x000001FC590D5000>
# <__main__.singleton object at 0x000001FC590D5000>

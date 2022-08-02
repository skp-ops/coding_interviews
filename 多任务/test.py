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

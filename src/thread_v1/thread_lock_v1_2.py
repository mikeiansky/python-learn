"""
锁使用，自增乱序的问题，在python3.10没有出现，但是在3.7的版本中出现了，这是为什么
其中一些解释
1. https://segmentfault.com/q/1010000041987131
2. https://blog.csdn.net/qq_34685213/article/details/132706689
"""

import threading
import time

count = 0
size = 10

# 3.10及之后的可以不需要这个
lock = threading.Lock()

print("locked :", lock.locked())

def stats(num):
    global count
    for i in range(num):
        # print("locked :", lock.locked())
        lock.acquire()
        # locked 方法返回当前锁的状态，被占用返回True,否则返回False，不会阻塞
        # lock.locked()        
        count = count + 1
        # time.sleep(1)
        lock.release()

t1 = threading.Thread(target=stats, args=(size,))
t2 = threading.Thread(target=stats, args=(size,))
# t3 = threading.Thread(target=stats, args=(size,))

t1.start()
t2.start()
# t3.start()


t1.join()
t2.join()
# t3.join()

print('complete and count value is :', count)
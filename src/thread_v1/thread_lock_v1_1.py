"""
锁使用
"""

import threading
import time

count = 0
product = None
done = False
lock = threading.Lock()
print('lock data:', lock)

# 生产
def produce():
    global count
    global product
    global done
    while(count<10):
        lock.acquire()
        if product is None:
            count = count + 1
            product = 'product-' + str(count)
            print('produce :' + product)
        lock.release()
    done = True

    print('produce complete')
    

# 消费
def consume():
    global count
    global product
    global done
    while not done:
        lock.acquire()
        if product is not None:
            print('consume :', product)
            product = None
        lock.release()

    print('consume complete')


t1 = threading.Thread(target=produce,)
t2 = threading.Thread(target=consume,)

t1.start()
t2.start()

t1.join()
t2.join()

print('app complete ... ')
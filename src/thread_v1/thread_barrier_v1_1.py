"""
thread 模块 barrier 
"""

import threading
import time

tb = threading.Barrier(3)

def hello(msg):
    # tb.n_waiting()
    # with tb:
    tb.wait()
    print('hello ', msg)

t1 = threading.Thread(target=hello, args=('t1',))
t2 = threading.Thread(target=hello, args=('t2',))
t3 = threading.Thread(target=hello, args=('t3',))
t1.start()
t2.start()
time.sleep(1)
t3.start()

t1.join()
t2.join()
t3.join()

print('phase two')
t1 = threading.Thread(target=hello, args=('t1',))
t2 = threading.Thread(target=hello, args=('t2',))
t3 = threading.Thread(target=hello, args=('t3',))
t1.start()
t2.start()
time.sleep(1)
t3.start()

t1.join()
t2.join()
t3.join()

print('app complete ... ')

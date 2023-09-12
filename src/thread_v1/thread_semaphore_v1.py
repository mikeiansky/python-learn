"""
线程信号量
"""

import threading
import time

# 信号量的数量
size = 5
sp = threading.Semaphore(size)

def hello(tag, msg):
    with sp:
        print(tag, 'accuire lock')
        print(tag, ' say hello ', msg)
        time.sleep(2)
        print(tag, 'release lock')


t1 = threading.Thread(target=hello, args=('t1', 'java'))
t2 = threading.Thread(target=hello, args=('t2', 'python'))
t3 = threading.Thread(target=hello, args=('t3', 'oracle'))
t4 = threading.Thread(target=hello, args=('t4', 'php'))
t5 = threading.Thread(target=hello, args=('t5', 'javascript'))
t6 = threading.Thread(target=hello, args=('t6', 'clang'))
t7 = threading.Thread(target=hello, args=('t7', 'c#'))

ts = [t1,t2,t3,t4,t5,t6,t7]

for t in ts:
    t.start()

for t in ts:
    t.join()

print('complete ...')


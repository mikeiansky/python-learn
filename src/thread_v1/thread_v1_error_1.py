"""
线程异常处理
"""

import threading
import sys

def custom_excepthook(exctype, value, traceback):
    print('custome except hook running')

def hello(msg):
    m = 0
    print('hello', msg)
    r = 11 / m

threading.excepthook = custom_excepthook

t1 = threading.Thread(target=hello, args=('t1',))
# threading.excepthook(threading=t1)
t1.start()


t1.join()

print('main complete ... ')
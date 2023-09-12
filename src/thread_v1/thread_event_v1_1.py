"""
线程事件
"""

import threading
import time

event = threading.Event()

print(id(event))

def hello(msg):
    # global event
    print('hello ', msg)
    time.sleep(2)
    event.set()
    # event = threading.Event()

t1 = threading.Thread(target=hello, args=('t1',))
t1.start()

print('before event wait')
event.wait()
# print(id(event))
print('after event wait')

t1.join()


print('complete ... ')
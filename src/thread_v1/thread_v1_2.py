"""
线程信息打印
"""

import threading
import time

age = 30
tag = 'mike'

def hello(msg, sleep):
    time.sleep(sleep)
    print('thread name ', threading.get_ident())
    print('hello-', msg, ' , age:', age, ', tag:', tag)

# 这里只有主线程激活
print('1 thread active count' , threading.active_count())

t1 = threading.Thread(target=hello, args=('t1', 1))
t2 = threading.Thread(target=hello, args=('t2', 2))
# t3 = threading.Thread(target=hello, args=('t3', 1))

# 这里只有主线程激活
print('2 thread active count' , threading.active_count())

t1.start()
t2.start()
# t3.start()

# 这里有两个线程激活了
print('3 thread active count' , threading.active_count())

for t in threading.enumerate():
    print("active thread : ",t)

t1.join()
t2.join()
# t3.join()

print('all complete')


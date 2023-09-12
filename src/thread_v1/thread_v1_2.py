"""
线程信息打印
"""

import threading
import time

age = 30
tag = 'mike'

def hello(msg, sleep, age=None, address=None):
    time.sleep(sleep)
    print('thread name ', threading.get_ident())
    print('hello-', msg, ' , age:', age, ', tag:', tag)
    print('current thread ', threading.current_thread())
    print('native id', threading.current_thread().native_id)
    print('is daemon thead', threading.current_thread().daemon)
    print('main thread : ' , threading.main_thread())
    print('time out max :', threading.TIMEOUT_MAX)
    print('age :', age, ', address :', address)
    # 不能将当前线程自己加入进去
    # threading.current_thread().join()

# 这里只有主线程激活
print('1 thread active count' , threading.active_count())

t1 = threading.Thread(target=hello, args=('t1', 1), 
                      kwargs={'age':25, 'address':'china'}, daemon=True)
t2 = threading.Thread(target=hello, args=('t2', 2), 
                      kwargs={'age':27, 'address':'america'})
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


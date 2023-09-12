"""
局部变量在线程中使用的限制
"""

import threading

count = 1

def hello(msg):
    # 可以直接用，但是不能修改其值，会出现异常
    # UnboundLocalError: local variable 'count' referenced before 
    # assignmentUnboundLocalError: local variable 'count' referenced before assignment
    # 如果要用的话，需要加上global关键字
    global count
    count = count + 1
    print('hello-msg-', msg, ', count:', count)

t1 = threading.Thread(target=hello, args=('t1',))
t2 = threading.Thread(target=hello, args=('t2',))

t1.start()
t2.start()

t1.join()
t2.join()

print('app complete ... ')
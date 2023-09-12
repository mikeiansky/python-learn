"""
线程读写锁
"""

import threading

# 创建一个 RLock 对象
lock = threading.RLock()

def func():
    with lock:
        print("Acquired lock by thread:", threading.current_thread().name)
        nested_func()

def nested_func():
    with lock:
        print("Acquired lock in nested function by thread:", threading.current_thread().name)

# 创建多个线程并启动
threads = []
for i in range(5):
    t = threading.Thread(target=func)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

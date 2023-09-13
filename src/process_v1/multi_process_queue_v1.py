"""
多进程使用queue共享数据
"""

import multiprocessing
import os
import time

# 多进程情况下这里会被调用了三次
print('init tag , pid: ', os.getpid(),'ppid: ', os.getppid())

def download(q):
    print('download start , id(q)', id(q))
    data = [12,44,11]
    data.append(89)
    time.sleep(2)
    q.put(data)
    print('download done')

def analyse(q):
    # 这里的queue和 download 不一样
    print('analyse start , id(q)', id(q), ', pid: ', os.getpid(), ', ppid: ', os.getppid())
    data = q.get()
    print('analyse data:', data)
    print('analyse done')

def main():
    queue = multiprocessing.Queue()
    print('main queue id:', id(queue))
    p1 = multiprocessing.Process(target=download, args=(queue,))
    p1.start()
    
    p2 = multiprocessing.Process(target=analyse, args=(queue,))
    p2.start()

    p1.join()
    p2.join()

    print('app complete ... , pid: ', os.getpid(), ', ppid: ', os.getppid())

if __name__ == '__main__':
    main()
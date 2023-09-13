"""
多进程共享数据
"""

import multiprocessing
import time
import os

def count(tag, data):
    # print(dir(data))
    # 这个数据是可以共享的
    # data.value = data.value + 1
    print('count @',tag,' pid:', os.getpid(), ', data:', data.value)    


def main():
    data = multiprocessing.Value('i', 45)
    print(data)

    p1 = multiprocessing.Process(target=count, args=('p1', data))
    p2 = multiprocessing.Process(target=count, args=('p2', data))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('app complete ... ')

if __name__ == '__main__':
    main()


"""
多进程，锁使用
"""

import multiprocessing
import time

def download(tag, lock, data):
    print('download tag :', tag, 'start ')
    with lock:
        data.value = 83
        time.sleep(2)

    print('download tag :', tag, 'complete ')

def stats(tag, lock, data):
    time.sleep(0.5)
    print('stats tag :', tag, 'start ')    
    with lock:
        print('stats data :', data.value)

    print('stats tag :', tag, 'complete ')

def main():
    data = multiprocessing.Value('i', 34)

    # 这两个lock有什么区别
    lock = multiprocessing.Manager().Lock()
    lock = multiprocessing.Lock()

    # multiprocessing.Condition
    # multiprocessing.Manager().Condition()

    p1 = multiprocessing.Process(target=download, args=('p1', lock, data))
    p2 = multiprocessing.Process(target=stats, args=('p2', lock, data))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()
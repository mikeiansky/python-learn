"""
多进程处理，其与多线程的区别,
测试下局部变量在线程中和进程中使用的区别
"""
import os
import multiprocessing
import threading
import time


t_name = 'thread-name'
t_num = 1
def t_hello(msg):
    global t_name, t_num
    t_name = t_name + str(t_num)
    time.sleep(1)
    t_num = t_num + 1
    print('t_hello', msg, os.getpid(), os.getppid())
    print('t_hello', msg, os.getpid(), os.getppid(), ', t_name:', t_name, ', t_num:', t_num)


p_name = 'multi_process'
p_num = 1
def p_hello(msg):
    # 这里在多进程的情况下，这些全局变量每次都会初始化，无法共享
    global p_name, p_num
    p_name = p_name + str(p_num)
    time.sleep(1)
    p_num = p_num + 1
    print('p_hello', msg, os.getpid(), os.getppid())
    print('p_hello:', msg, ', p_name:', p_name, ', p_num:', p_num)


def main():   

    t1 = threading.Thread(target=t_hello, args=('t1',))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=t_hello, args=('t2',))
    t2.start()    
    t2.join()

    mp1 = multiprocessing.Process(target=p_hello, args=('mp1',))
    mp1.start()
    mp2 = multiprocessing.Process(target=p_hello, args=('mp2',))
    mp2.start()
    mp1.join()
    mp2.join()

    mp1 = multiprocessing.Process(target=p_hello, args=('mp1',))
    mp1.start()
    mp2 = multiprocessing.Process(target=p_hello, args=('mp2',))
    mp2.start()
    mp1.join()
    mp2.join()

    print('main complete , pid :', os.getpid(), os.getppid())


if __name__ == '__main__':
    main()
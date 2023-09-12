"""
基础线程池用法
"""

from concurrent.futures.thread import ThreadPoolExecutor
import time

pool = ThreadPoolExecutor(6)

def hello(tag, msg):
    print(tag, 'start')
    print(tag, 'say hello', msg)
    time.sleep(1)
    print(tag, 'complete')

f1 = pool.submit(hello, 't1', 'java')
f2 = pool.submit(hello, 't2', 'oracle')
f3 = pool.submit(hello, 't3', 'php')
f4 = pool.submit(hello, 't4', 'clang')
f5 = pool.submit(hello, 't5', 'node')

f1.result()
f2.result()
f3.result()
f4.result()
f5.result()

def map_hello(args):
    tag, msg = args
    print(tag, 'start')
    print(tag, 'say hello', msg)
    time.sleep(1)
    print(tag, 'complete')



pool.map(map_hello, [('m1','java'), ('m2','oracle')])

print('main complete')

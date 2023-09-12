"""
多进程应用
"""

from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def hello( tag, msg):
    print( tag, 'say hello', msg)

if __name__ == '__main__':
    print('main start')
    multiprocessing.freeze_support()
    with ProcessPoolExecutor() as executor:
        sf = executor.submit(hello, *('p1','java',))
        sf.result()
"""
多进程中manager使用
"""

import multiprocessing

def download(tag, data):
    print('download type(data):', type(data))
    data['download'] = 'put very much data!'
    print('download tag:', tag, ', data:', data)

def analyse(tag, data):
    print('analyse type(data):', type(data))
    data['analyse'] = 'this is good data!'
    print('analyse tag:', tag, ', data:', data)

def main():
    # 这个数据可以共享
    md = multiprocessing.Manager().dict()
    md['main'] = 'multi - main'

    p1 = multiprocessing.Process(target=download, args=('p1', md))    
    p2 = multiprocessing.Process(target=analyse, args=('p2', md))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('main complete ... ')

if __name__ == '__main__':
    main()
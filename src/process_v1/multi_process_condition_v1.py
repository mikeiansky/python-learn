"""
多进程，条件变量
"""

import multiprocessing
import time

def produce(tag, not_full_condition, not_empty_condition, data):    
    print('produce tag:', tag, ' start')
    num = 1
    with not_full_condition:
        while True:
            while len(data) >= 10:
                not_full_condition.wait()
            
            time.sleep(0.2)
            pd = tag+'-'+str(num)
            num = num + 1
            data.append(pd)
            print(tag,'produce create data:', pd)

            not_empty_condition.notify_all()

    # print('produce tag:', tag, ' complete')

def consume(tag, not_full_condition, not_empty_condition, data):
    print('consume tag:', tag, ' start')
    with not_empty_condition:
        while True:
            while len(data) <= 0:
                not_empty_condition.wait()

            time.sleep(0.2)
            cd = data.pop()
            print(tag,'consume data:', cd)

            not_full_condition.notify_all()


    print('consume tag:', tag, ' complete')

def main():
    data = multiprocessing.Manager().list()

    lock = multiprocessing.Lock()
    not_full_condition = multiprocessing.Condition(lock)
    not_empty_condition = multiprocessing.Condition(lock)

    p1 = multiprocessing.Process(target=produce, args=('p1', not_full_condition, not_empty_condition, data))
    p1.start()
    
    c1 = multiprocessing.Process(target=consume, args=('c1', not_full_condition, not_empty_condition, data))
    c1.start()

    p1.join()
    c1.join()

    print('main complete ... ')

if __name__ == '__main__':
    main()
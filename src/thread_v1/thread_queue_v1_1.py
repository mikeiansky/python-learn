"""
线程中queue的使用
"""

import threading
import queue
import time

share_data = queue.Queue()

def produce(tag):
    num = 0
    while True:
        data = tag + '-create data-' + str(num)
        share_data.put(data)
        num = num + 1
        time.sleep(1)

def consume(tag):    
    while True:
        data = share_data.get()
        print(tag, 'get data [', data, ']')
        share_data.task_done()



tp = []
p1 = threading.Thread(target=produce, args=('p1',))
p2 = threading.Thread(target=produce, args=('p2',))
p3 = threading.Thread(target=produce, args=('p3',))
tp.append(p1)
tp.append(p2)
tp.append(p3)

c1 = threading.Thread(target=consume, args=('c1',))
c2 = threading.Thread(target=consume, args=('c2',))
tp.append(c1)
tp.append(c2)

for t in tp:
    t.start()

for t in tp:
    t.join()

print('main complete ')

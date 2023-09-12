"""
多生产者，多消费者模型，
这个可以达到
"""

import threading

share_data = []
max_data = 5
max_produce = 6
max_consume = 6
produce_num = 0
consume_num = 0

lock = threading.Lock()
not_full_condition = threading.Condition(lock)
not_empty_condition = threading.Condition(lock)
produce_condition = threading.Condition(lock)
consume_condition = threading.Condition(lock)


def produce(tag, msg, num):
    global produce_num
    for i in range(num):        
        with lock:
            while produce_num >= max_produce:
                produce_condition.wait()
            produce_num = produce_num + 1
            while len(share_data) >= max_data:
                not_full_condition.wait()

        data = tag + '-produce-'+msg+'-'+str(i)
        
        # 这里可能是耗时操作
        print('produce create data', data)

        with lock:
            share_data.append(data)
            produce_num = produce_num - 1
            consume_condition.notify_all()
            not_empty_condition.notify_all()            

def consume(tag, msg):  
    global consume_num  
    while True:        
        with lock:
            while consume_num >= max_consume:
                consume_condition.wait()
            consume_num = consume_num +1
            while len(share_data) <= 0:
                not_empty_condition.wait()
            data = share_data.pop()            
            

        # 这里可能是耗时操作
        print(tag, msg, 'consume data', data)

        with lock:
            consume_num = consume_num - 1
            consume_condition.notify_all()
            not_full_condition.notify_all()


size = 100
td = []
p1 = threading.Thread(target=produce, args=('p1', 'java', size))
p2 = threading.Thread(target=produce, args=('p2', 'python', size))
p3 = threading.Thread(target=produce, args=('p3', 'clang', size))
td.append(p1)
td.append(p2)
td.append(p3)

c1 = threading.Thread(target=consume, args=('c1', 'java'))
c2 = threading.Thread(target=consume, args=('c2', 'python'))
c3 = threading.Thread(target=consume, args=('c3', 'clang'))
td.append(c1)
td.append(c2)
td.append(c3)

for t in td:
    t.start()

for t in td:
    t.join()

print('main complete ... ')



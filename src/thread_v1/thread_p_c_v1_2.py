"""
多线程-生产者消费者模型，这个生产者消费者模型，
有问题，同一时间只能有一个进行生成或者消费
"""

import threading

share_data = []
max = 50

lock = threading.Lock()
not_full_condition = threading.Condition(lock)
not_empty_condition = threading.Condition(lock)


def produce(tag, msg, num):
    with not_full_condition:
        for i in range(num):
            while len(share_data) >= max:
                not_full_condition.wait()
            data = tag + '-produce-'+msg+'-'+str(i)
            print(data)
            share_data.append(data)
            not_empty_condition.notify_all()

def consume(tag, msg, num):
    with not_empty_condition:
        while True:
            while len(share_data) <= 0:
                not_empty_condition.wait()
            data = share_data.pop()
            print(tag, msg, num, 'consume data', data)
            not_full_condition.notify_all()



td = []
p1 = threading.Thread(target=produce, args=('p1', 'java', 100))
p2 = threading.Thread(target=produce, args=('p2', 'python', 100))
p3 = threading.Thread(target=produce, args=('p3', 'clang', 100))
td.append(p1)
td.append(p2)
td.append(p3)

c1 = threading.Thread(target=consume, args=('c1', 'java', 5))
c2 = threading.Thread(target=consume, args=('c2', 'python', 6))
c3 = threading.Thread(target=consume, args=('c3', 'clang', 7))
td.append(c1)
td.append(c2)
td.append(c3)

for t in td:
    t.start()

for t in td:
    t.join()

print('main complete ... ')



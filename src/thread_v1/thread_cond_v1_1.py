"""
线程条件锁对象
"""

import threading

lock = threading.Lock()
not_full_condition = threading.Condition(lock)
not_empty_condition = threading.Condition(lock)

total = 10
complete = False
data = []
max = 3

def produce():
    with lock:       
        for i in range(total):
            # 用while 是因为wait被唤醒后，可能复合的条件已经不存在需要，重新进入等待
            while len(data) >= max:
                # 这里会释放当前锁
                not_full_condition.wait()
            product = 'product' + str(i)
            data.append(product)
            print('create :', product)
            # notify 并不会释放当前锁
            not_empty_condition.notify_all()
        global complete
        complete = True
        print('produce complete ... ')

def consume():
    with lock:
        global complete
        while not complete:
            while len(data) == 0:
                not_empty_condition.wait()
            product = data.pop()
            print('consume :', product)
            not_full_condition.notify_all()
            
    
        print('consume complete ... ')


produce_thread_1 = threading.Thread(target=produce)
consume_thread_1 = threading.Thread(target=consume)

produce_thread_1.start()
consume_thread_1.start()

produce_thread_1.join()
consume_thread_1.join()

print('app complete ... ')
"""
生产者消费者模型
"""

import threading
import time

# 共享的数据列表
shared_data = []
# 用于同步的条件变量
condition = threading.Condition()

# 生产者线程函数
def producer(name):
    while True:
        # 模拟生产数据
        data = name + " - data"
        # 获取条件变量锁
        with condition:
            # 将数据放入共享列表
            shared_data.append(data)
            print(f"Producer {name} produced: {data}")
            # 通知等待的消费者线程
            condition.notify()
        # 等待一段时间
        time.sleep(1)

# 消费者线程函数
def consumer(name):
    while True:
        # 获取条件变量锁
        with condition:
            while len(shared_data) == 0:
                # 等待生产者线程生产数据
                condition.wait()
            # 从共享列表获取数据
            data = shared_data.pop(0)
            print(f"Consumer {name} consumed: {data}")
        # 模拟处理数据
        time.sleep(2)

# 创建生产者线程
producers = []
for i in range(3):
    t = threading.Thread(target=producer, args=(f"Producer-{i+1}",))
    producers.append(t)
    t.start()

# 创建消费者线程
consumers = []
for i in range(2):
    t = threading.Thread(target=consumer, args=(f"Consumer-{i+1}",))
    consumers.append(t)
    t.start()

# 等待所有生产者线程完成
for t in producers:
    t.join()

# 停止消费者线程
for t in consumers:
    t.join()

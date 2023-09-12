"""
多线程导致的错误统计,
高版本的自增已经完善了，不会出现乱序
"""
import threading

count = 0
age = 20
num = 100000

def stats():
    global count, age
    for i in range(num):
        tmp = count
        age = 20
        age = age + 30
        count = tmp + 1

t1 = threading.Thread(target=stats)
t2 = threading.Thread(target=stats)
t3 = threading.Thread(target=stats)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print('main complete count', count)

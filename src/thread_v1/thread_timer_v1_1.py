"""
定时器
"""

import threading

def hello(msg):
    print('hello ', msg)


timer = threading.Timer(2, hello,('timer', ))
timer.start()

timer.join()

print('main complete')
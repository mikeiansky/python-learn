"""
    这里是装饰器v2版本
"""

def log(func):

    def wrapper(*args, **kwargs):
        print('log start ... ')
        result = func(*args, **kwargs)
        print('log complete ... ')
        return result
    
    return wrapper

def count(num):
    def count_wrap(func):
        def wrapper(*args, **kwargs):
            print('count start --- ', num)
            result = func(*args, **kwargs)
            print('count complete --- ', num)
            return result
        return wrapper
    return count_wrap

@log
@count(5)
@log
@count(3)
def hello(msg):
    print('hello -->', msg)
    return "hello-"+ msg

hello('mike')


"""
装饰器v4版本
"""

def log(func):
    def wrapper(*arg, **kwargs):
        print('log start')
        result = func(*arg, **kwargs)
        print('log complete')

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

@count(5)
@log
@count(3)
def hello(msg):
    print('hello', msg)


if __name__ == "__main__":
    hello('world')
"""
装饰器
"""


def log(func):
    """
        不带参数的装饰器
    """

    def wrap(*args, **kwargs):
        print('log start ... ')
        result = func(*args, **kwargs)
        print('log complete ... ')
        return result
    return wrap

def count(num):
    def count_decorate(func):
        def wrap(*args, **kwargs):
            print("count decorate start num : ", num)
            result = func(*args, **kwargs)
            print("count decorate complete num : ", num)
            return result
        return wrap
    return count_decorate

@count(24)
@log
@count(59)
def hello(msg):
    print('this is hello, msg:', msg)


hello('mike')
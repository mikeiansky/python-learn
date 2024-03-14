
def count(value):

    def lc(func):
        def wrapper(*args, **kwargs):
            print('count start --- ', value)
            result = func(*args, **kwargs)
            print('count complete --- ', value)
            return result
        return wrapper
    return lc 

def log(func):
    def wrapper(*args, **kwargs):
        print('log start ... ')
        result = func(*args, **kwargs)
        print('log complete ... ')
        return result

    return wrapper

@count(11)
@log
@count(22)
def hello(msg):
    print('hello -->', msg)



if __name__ == '__main__':
    hello('test')
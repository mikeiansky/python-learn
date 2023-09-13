"""
使用对象或者类来进行注解
"""


class Dec():
    
    def __init__(self):
        pass

    def log(self, func):
        def wrapper(*args, **kwargs):
            print('dec log start')
            result = func(*args, **kwargs)
            print('dec log complete')
            return result
        return wrapper
    
    def count(self, num):
        def de_count(func):
            def wrapper(*args, **kwargs):
                print('count start', num)
                result = func(*args, **kwargs)
                print('count complete', num)
                return result
            return wrapper        
        return de_count
    
    @staticmethod
    def echo(func):
        def wrapper(*args, **kwargs):
            print('echo start ... ')
            result = func(*args, **kwargs)
            print('echo complete ... ')
            return result
        
        return wrapper
    
    @classmethod
    def under(cls, func):
        def wrapper(*args, **kwargs):
            print('under start ... ')
            result = func(*args, **kwargs)
            print('under complete ... ')
            return result
        
        return wrapper

dec = Dec()

class Info():

    @dec.log
    @dec.count(4)
    @Dec.echo
    @Dec.under
    def test(self,msg):
        print('info', msg)



@Dec.under
@Dec.echo
@dec.count(5)
@dec.log
@dec.count(9)
@dec.log
def hello(msg):
    print('hello', msg)


hello('v3')

# Dec.under('cc')
print('----------- ')
info = Info()
info.test('yes')
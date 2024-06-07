"""
函数参数使用 v2 版本
"""

def use_arg(a1, a2, a3):
    print(a1, a2, a3)

def use_book(a1, book=None, price=0, address=None):
    print(a1, book, price, address)
    
def lf(*a):
    print(a)
    print(*a)
    
def df(**ka):
    print(ka)
    
def cf1(*la, **ka):
    print('la', la)
    print('ka', ka)
    
def cf2(*la, **ka):
    print('la', la)
    print('ka', ka)

def run():
    use_arg(11, 22, 33)
    # use_arg(11, 22, 33)
    al = [111, 222, 333]
    use_arg(*al)        
    print(al)
    # print(**al)
    ad = {'book':'java', 'price':33.33, 'address': 'shenzhen'}
    print(ad)
    # print(*ad)
    # print(**ad)
    use_book(11, **ad)
    lf(1, 2, 3)
    df(name='ian',age=18,address='china')
    
    cf1(1, 2, 3, 4, city='zhen')
    
    cf1(1, 2, 3, 4, city='zhen2')

if __name__ == "__main__" : 
    run()
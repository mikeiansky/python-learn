"""
字符串
"""

def test():
    coll = ['one', 'two', 'three']
    head = 'ian'
    tail = 'foot'
    comp = head.join(tail)
    print(comp)
    print('coll join', ','.join(coll))
    print(head.split('a'))
    pass




if __name__ == '__main__':
    pass
    test()
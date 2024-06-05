"""
测试id的变化情况
"""

def change_value():
    a = 1
    print(id(a))    
    b = a
    print(id(b))
    a = a + 2
    print(id(a))
    # print(id(1))
    print(id(b))


if __name__ == "__main__":
    change_value()
    print('test id ')
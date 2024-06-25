"""
函数基础v2
"""

tag = 'hello'

def changeValue():
    print(tag)    
    # tag = 'world'
    # 这里会报错，不能再函数里面，修改全局变量
    # print(tag) 
    
    squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
    for v in squared:
        print(v)

if __name__ == "__main__" :
    changeValue()
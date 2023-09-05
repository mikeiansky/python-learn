"""
定制类的一些用法，主要是使用一些内置的自定义函数大部分是以__xxx()__形式出现的
比如__len__
"""

from typing import Any


class CustomObj():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getitem__(self, key):
        print("get item key :", key)
        if isinstance(key, slice) :
            print('start :', key.start)
            print('stop :', key.stop)
            print('step :', key.step)
        return 'custom'
    
    def __getattr__(self, name):
        print("get attr value is ", name)
        return 0
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("custom object call , type(args)", type(args)," args :", args," , type(kwds)", type(kwds), ", kwds :", kwds)
    

co = CustomObj('mike', 25)
print(co['12'])
print(co[0])
print(co[20])
print(co.address)
print(co.name)

print(dir(CustomObj))
print(dir(co))
# print(len(co))

co[1:10:5]
co[:]

co(12,33,44,k1='mike', k22=34)
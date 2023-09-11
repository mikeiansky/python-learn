"""
方法中参数传递
"""

age = 1024
print(id(age))
print(age)
age = 40
print(id(age))
print(age)
# age = 256
# print(id(age))
# print(age)

data = [10, 23, 67]
print(id(data))
print(data)

def change_base(base):
    print('base 1 id:', id(base))
    base = 1024
    print('base 2 id:', id(base))

def change_obj(obj):
    print('obj id:', id(obj))
    obj[2] = 44

change_base(age)
print(id(age))
print(age)

change_obj(data)
print(id(data))
print(data)

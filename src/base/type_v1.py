"""
类型数据
"""
from collections.abc import Iterable

# 这里会被编译为一个元组
data_1 = (1,)
print("data_1",data_1)
print(type(data_1))
print(isinstance(data_1, Iterable))

# 这里会被编译为一个整型
data_2 = (1)
print("data_2",data_1)
print(type(data_2))
print(isinstance(data_2, Iterable))

# 这里会被编译为一个字符串
data_3 = ('mike')
print('data_3', data_3)
print(type(data_3))
print(isinstance(data_3, Iterable))

# 这里会被编译为一个元组
data_4 = ('ian',)
print(len(data_4))
print('data_4', data_4)
print(type(data_4))
print(isinstance(data_4, Iterable))

data_5 = (35, 'aa')
print(len(data_5))
print('data_5', data_5)
print('type(data_5)', type(data_5))
print(isinstance(data_5, Iterable))

data_6 = (351, 'aa1',)
print(len(data_6))
print('data_6', data_6)
print('type(data_6)', type(data_6))
print(isinstance(data_6, Iterable))



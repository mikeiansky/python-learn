"""
变量的使用方式
"""

sv = (23, 44)
age1, age2 = sv

print(age1)
print(age2)

def hello(*args):
    print('hello arg type', type(args))
    for a in args:
        print(type(a), a)

hello(sv)
hello(*sv)
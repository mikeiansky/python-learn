"""
metclass的高级用法
"""

def echo(self, msg):
    # 如果这个方法是被实例化的对象所调用的话，那么self就代表这个实例化对象本身
    print('echo msg:', msg)

class PersonMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print('meta new for person start ==>')
        print('bases :', bases)
        print('attrs :', attrs)
        # 动态的添加一个方法
        attrs['meta_echo'] = echo
        attrs['tag'] = 'meta-tag'
        print('meta new for person complete ==>')
        return type.__new__(cls, name, bases, attrs)


class Person(metaclass=PersonMetaclass):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self,msg):
        print(self.name, 'say hello :', msg)

print('before new person')
p = Person('mike', 29)
print(dir(p))
p.hello('shenzhen')
# 调用动态添加的方法
p.meta_echo('guangdong')
# 调用动态添加的字段
print('person-meta-tag is', p.tag)
print('after new person')




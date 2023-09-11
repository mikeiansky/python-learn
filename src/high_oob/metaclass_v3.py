"""
这里是metaclass v3 版本
"""

def say_hello(self,msg):
    print("body say hello", msg, self.name, self.age)

class BodyMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['tag'] = 'tag-meta'
        attrs['hello'] = say_hello
        return type.__new__(cls, name, bases, attrs)

class Body(metaclass=BodyMetaclass):

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


body = Body('mike', 32)

print(body.name)
print(body.age)
print(body.tag)
body.hello('meta')
        
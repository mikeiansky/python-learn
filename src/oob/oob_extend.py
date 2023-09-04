"""
面对对象继承测试
"""

class Animal():

    def __init__(self, name):
        print('init animal , name :', name)

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
        print('dog init')

a1 = Animal('normal')

dog = Dog('dog')

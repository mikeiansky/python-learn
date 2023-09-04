"""
自定义类的基础用法，以及数据比较
"""

class MetaObj():

    def __init__(self, name) -> None:
        self.name = name

    def hello(self, msg):
        print('meta obj say hello, msg :', msg)

def echo(oo, msg):
    # 这里oo 其实就是 self, 按照规范的话，应该将变量命名为self
    print('oo value is', oo)
    print('value is', msg)

print('--------- tc1 ')
tc1 = type('Mike1')
print('tc1 :',tc1)
print('type(tc1) :',type(tc1))

print('--------- tc2 ')
tc2 = type('Mike2', (object,), dict())
print('tc2 :',tc2)
print('type(tc2) :',type(tc2))
print('dir(tc2) :',dir(tc2))
tc2_obj = tc2()
print('tc2_obj :',tc2_obj)
print('type(tc2_obj) :',type(tc2_obj))
print('dir(tc2_obj) :',dir(tc2_obj))

print('--------- tc3 ')
tc3 = type("Mike3", (object,), dict(say=echo))
print('tc3 :', tc3)
print('type(tc2) :',type(tc3))
print('dir(tc3) :',dir(tc3))

tc3_obj = tc3()
print('tc3_obj :', tc3_obj)
print('type(tc3_obj) :',type(tc3_obj))
print('dir(tc3_obj) :',dir(tc3_obj))
tc3_obj.say('world')

print('--------- MetaObj ')
print('MetaObj :', MetaObj)
print('type(MetaObj) :', type(MetaObj))
print('dir(MetaObj) :', dir(MetaObj))
mo1 = MetaObj('mc')
print('mo1 :', mo1)
print('type(mo1) :', type(mo1))
print('dir(mo1) :', dir(mo1))

print('---------- mt1')
mt1 = type('MetaObj', (object,), dict())
print("mt1 :",mt1)
print("type(mt1) :",type(mt1))
print("dir(mt1) :",dir(mt1))
print('isinstance(mt1, MetaObj) :',isinstance(mt1, MetaObj))
print('mt1 == MetaObj :', mt1 == MetaObj)

print('---------- mt2')
mt2 = type('MetaObj', (MetaObj,), dict())
print("mt2 :",mt2)
print("type(mt2) :",type(mt2))
print("dir(mt2) :",dir(mt2))
print('isinstance(mt2, MetaObj) :',isinstance(mt2, MetaObj))
print('mt2 == MetaObj :', mt2 == MetaObj)
mt2_obj = mt2('from-type-mt2')
print("mt2_obj :",mt2_obj)
print("type(mt2_obj) :",type(mt2_obj))
print("dir(mt2_obj) :",dir(mt2_obj))
print('isinstance(mt2_obj, MetaObj) :',isinstance(mt2_obj, MetaObj))
print('mt2_obj == MetaObj :', mt2_obj == MetaObj)






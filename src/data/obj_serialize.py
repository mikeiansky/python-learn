"""
对象序列化
"""
import json
from obj import Person

person = Person("mike", "28")
print(person)

key1 = "python"
key2 = 3
kr = key1 + str(key2)
print("kr value is ", kr)

# json.dumps与json.dump有什么区别
result = json.dumps(person.to_dict())
print(result)

def person_encoder(obj):
    print('person encoder obj : ', obj)
    if isinstance(obj, Person):
        return obj.__dict__
    return obj

def person_decoder(obj):
    print('person decoder obj : ', obj)
    if 'name' in obj and 'age' in obj:
        return Person(obj['name'], obj['age'])    
    return obj

# 不能这样运行
# p2 = json.loads(result, cls=Person.__class__)
# print(p2)

# 加载方式一，这里的**d代表什么意思?
p2 = json.loads(result, object_hook=lambda d: Person(**d))
print(p2)

# 加载方式二
p3 = json.loads(result, object_hook=Person.from_dict)
print(p3)

# 这里能直接打印person.__dict__, 是可以的
print("person.__dict__")
print(person.__dict__)

# 将person 放入到字典里面进行序列化
kd = {
    'app' : 'study',
    'version' : 3,
    'person' : person
}
print("kv.person is person," , isinstance(kd['person'], Person))
kv_dumps = json.dumps(kd, default=person_encoder)
print(kv_dumps)

# 无自定义加载
kv_loads1 = json.loads(kv_dumps)
print(kv_loads1)
print("kv_loads.person is person," , isinstance(kv_loads1['person'], Person))

# 有自定义加载
kv_loads2 = json.loads(kv_dumps, object_hook=person_decoder)
print(kv_loads2)
print("kv_loads.person is person," , isinstance(kv_loads2['person'], Person))
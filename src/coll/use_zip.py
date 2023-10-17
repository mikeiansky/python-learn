"""
zip的使用
"""


key = [22, 39, 77]

value = ['python','java','clang']

result = zip(key, value)

print(type(result))

print(result)

# for k,v in result:
#     print(k, v)

for r in result:
    print(r, type(r), r[0], r[1])

print('----3')
for r in result:
    print(r, type(r))


books = [(22, 'oracle'),(89, 'java'),(74,'test')]
for id, title in books:
    print(id, title)
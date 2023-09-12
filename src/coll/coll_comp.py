"""
集合类的推导式
"""

# 列表推导式生成列表，基本使用
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)
ld = ['ll-' + str(d) for d in data]
print(type(ld))
print(ld)

# 列表推导式生成列表，推导式中带有if 条件
if_ld = [ 'o-'+ str(d) if d % 2 == 0 else d for d in data]
print(type(if_ld))
print(if_ld)

# 列表推导式生成生成器，推导式中带有if 条件
gen_ld = ( 'o-'+ str(d) if d % 2 == 0 else d for d in data)
print(type(gen_ld))
print(gen_ld)
for gd in gen_ld:
    print(gd)

# 列表推导式生成字典，基本使用
dict_dd = {'key'+str(d):d for d in data}
print(type(dict_dd))
print(dict_dd)

# 列表推导式生成字典，推导式中使用if条件，推导式中的if和else只能影响key部分
if_dict_dd = {'o-k'+str(d) if d % 2 == 0 else 'j-k'+str(d): 20 + d for d in data}
print(type(if_dict_dd))
print(if_dict_dd)

rdd = {'key1': 1 , 'key2': 2, 'key3': 2, 'key2': 2, 'key2': 2}

# 列表推导式生成集合
sd = {'col-'+str(d) for d in data}
print(type(sd))
print(sd)

# 集合推导式生成列表
lsd = [si for si in sd]
print(type(lsd))
print(lsd)

# 字典推导式生成列表
print(if_dict_dd)
dld = [key for key in if_dict_dd]
print(type(dld))
print(dld)

# 字典推导式生成字典
dd_ld = {'ok-'+kd : 'ov-'+str(vd) for kd , vd in if_dict_dd.items()}
print(type(dd_ld))
print(dd_ld)

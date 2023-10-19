"""
最小二乘法的梯度下降法,
求 y=(x-1)^2的最值
"""

theta = 1.01

min = 2**32

x = 100
count = 0
stop = False
while not stop and count <= 10:
    count = count + 1
    s = (x-2)
    print('s ', s)
    x = x - theta * s 
    if x < min:
        min = x
    
    if abs(min - 2) <= 0.01:
        stop = True
    print(min)

print('final min : ', min)

print(x)


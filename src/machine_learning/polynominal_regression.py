"""
二次多项式回归
"""

import numpy as np
import matplotlib.pyplot as plt
import time

rng2 = np.random.default_rng()

size = 20
x = np.linspace(1, 20, size)
y = x * 2.5 + (x ** 2) * 1.7 +  ((np.arange(size) + 2) * (1.5* rng2.standard_normal(size)))

x_mean = x.mean()
x_std = x.std()

def standardize(v):
    return (v - x_mean)/x_std
    # return v

x_s = standardize(x)


r_x = np.vstack([np.ones(x_s.shape[0]), x_s, x_s ** 2]).T

theta = np.random.rand(3)

eta = 1e-3

def f(v):
    # print(v.shape, theta.shape)
    return np.dot(v, theta)

def Error(xx, yy):
    return 0.5 * np.sum((yy - f(xx)) ** 2)


diff = 1
count = 0
error = Error(r_x, y)

def mes(xx, yy):
    return (1/xx.shape[0]) * np.sum((yy - f(xx)) ** 2)

errors = []

while diff > 1e-2:
    # print((f(r_x) - y))

    vv = f(r_x) - y

    gradient = np.dot(vv, r_x)

    print('gradient', gradient, 'vv.shape: ', vv.shape , ', r_x.shape : ', r_x.shape)
    
    theta = theta - eta * gradient

    count += 1
    current_error = Error(r_x, y)
    diff = error - current_error
    error = current_error

    errors.append(mes(r_x,y))

    print('theta0 :',theta, ", count :",count, ", diff :", diff)

    # time.sleep(1)



plt.scatter(x_s, y, label='original data')
plt.plot(x_s, f(r_x), color='red')
plt.show()


e_x = np.arange(len(errors))
plt.plot(e_x, errors)
plt.show()

# print(r_x)
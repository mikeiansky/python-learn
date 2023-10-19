import numpy as np
import matplotlib.pyplot as plt
import time

rng2 = np.random.default_rng()

size = 20
x = np.linspace(1, 20, size)
y = x * 2.5 + (x ** 2) * 1.7 + ((np.arange(size) + 2) * (1.5 * rng2.standard_normal(size)))

x_mean = x.mean()
x_std = x.std()


def standardize(v):
    return (v - x_mean) / x_std


x_s = standardize(x)

r_x = np.vstack([np.ones(x_s.shape[0]), x_s, x_s ** 2]).T

theta = np.random.rand(3)

eta = 1e-3


def f(v):
    return np.dot(v, theta)


def Error(xx, yy):
    return 0.5 * np.sum((yy - f(xx)) ** 2)


diff = 1
count = 0
error = Error(r_x, y)

while diff > 1e-2:
    gradient = np.dot(f(r_x) - y, r_x)

    
    print(gradient)

    theta = theta - eta * gradient
    
    count += 1
    current_error = Error(r_x, y)
    diff = error - current_error
    error = current_error

    print('theta:', theta, ', count:', count, ', diff:', diff)
    time.sleep(1)


plt.scatter(x_s, y, label='original data')
plt.plot(x_s, f(r_x), color='red')
plt.show()

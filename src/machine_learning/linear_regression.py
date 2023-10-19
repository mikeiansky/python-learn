import numpy as np
import matplotlib.pyplot as plt

rng2 = np.random.default_rng()

size = 20
x = np.linspace(0, 20, size)
y = x * 2 + rng2.standard_normal(size) * 3

# 构建设计矩阵
X = np.column_stack((x, np.ones(size)))

# 使用基础函数模拟实现 np.linalg.lstsq()
XTX = np.dot(X.T, X)
XTy = np.dot(X.T, y)
params = np.linalg.solve(XTX, XTy)

# 提取斜率和截距
slope, intercept = params

# 计算拟合直线的预测值
y_pred = slope * x + intercept

# 绘制原始数据和拟合直线
# plt.scatter(x, y, label='Original Data')
# plt.plot(x, y_pred, color='red', label='Linear Regression')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

print("斜率:", slope)
print("截距:", intercept)



theta0 = np.random.rand()
print(theta0)
theta1 = np.random.rand()
print(theta1)

x_mean = x.mean()
x_std = x.std()

def standardize(v):
    return (v - x_mean)/x_std

x_s = standardize(x)

def f(v):
    return theta0 + theta1 * v

def Error(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


eta = 1e-3

diff = 1
count = 0
error = Error(x_s, y)

while diff > 1e-2:

    tmp_theta0 = theta0 - eta * np.sum((f(x_s)- y))
    tmp_theta1 = theta1 - eta * np.sum((f(x_s)- y) * x_s)

    theta0 = tmp_theta0
    theta1 = tmp_theta1

    current_error = Error(x_s, y)
    diff = error - current_error
    error = current_error
    count += 1

    print('theta0 :',theta0, " , theta1: ", theta1, ", count :",count, ", diff :", diff)



plt.scatter(x_s, y, label='Original Data')
plt.plot(x_s, y_pred, color='green', label='Linear Regression')
plt.plot(x_s, f(x_s), color='red', label='Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# print(f(x_s))

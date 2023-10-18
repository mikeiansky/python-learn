import numpy as np
import matplotlib.pyplot as plt

rng2 = np.random.default_rng()

size = 20
x = np.linspace(0, 20, size)
y = x * 2 + rng2.standard_normal(size) * 4

# 构建设计矩阵
X = np.column_stack((x, np.ones(size)))
# print(x)
# print(X)
# print(X.T)
X = x

# 使用基础函数模拟实现 np.linalg.lstsq()
XTX = np.dot(X.T, X)
XTy = np.dot(X.T, y)

print(XTX)
print(XTy)

# params = np.linalg.solve(XTX, XTy)

# print(params)

# 提取斜率和截距
# slope, intercept = params

# 计算拟合直线的预测值
# y_pred = slope * x + intercept

# 绘制原始数据和拟合直线
# plt.scatter(x, y, label='Original Data')
# plt.plot(x, y_pred, color='red', label='Linear Regression')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# print("斜率:", slope)
# print("截距:", intercept)

import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据
np.random.seed(0)
X = np.linspace(-3, 3, 100)
y = 0.5 * X**2 + X + 2 + np.random.normal(0, 1, size=X.shape)

# 构建特征矩阵
X_poly = np.column_stack((X, X**2))

# 使用最小二乘法计算回归系数
coefficients = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y

# 预测
X_test = np.linspace(-3, 3, 100)
X_test_poly = np.column_stack((X_test, X_test**2))
y_pred = X_test_poly @ coefficients

# 绘制结果
plt.scatter(X, y, label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Quadratic Polynomial Regression')
plt.legend()
plt.show()

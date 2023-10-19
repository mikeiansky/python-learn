"""
numpy 基础
"""

import numpy as np
from numpy import newaxis
import matplotlib.pyplot as plt


a = np.arange(5)

b = np.arange(15).reshape(5, 3)

print('a')
print(a)
print('b')
print(b)

c = np.dot(a, b)
print('c')
print(c)







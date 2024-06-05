"""
pytorch v1版本
"""

import torch
import numpy as np


arr = np.asarray([4, 5, 6, 7])
ts = torch.from_numpy(arr)
print(ts)
print(type(ts))
print(ts.numpy())

td = torch.zeros(20, dtype=torch.int64)
print(td)
print(td.numpy())

a = torch.tensor(1)
print(a)
print(a.item())

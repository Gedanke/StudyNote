# -*- coding: utf-8 -*-


import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a * b)
# 对应位置相乘: Get array([[ 5, 12],
#             [21, 32]])
print(a.dot(b))
# 矩阵乘法，Get array([[19, 22],
#             [43, 50]])

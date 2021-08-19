# -*- coding: utf-8 -*-

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print(np.inner(a, b))
# 点乘: Get 70
print(np.outer(a, b))
# 叉乘: Get
# array([[5, 6, 7, 8],
#        [10, 12, 14, 16],
#        [15, 18, 21, 24],
#        [20, 24, 28, 32]])
print(np.multiply(a, b))
# 对应项相乘: Get array([ 5, 12, 21, 32])

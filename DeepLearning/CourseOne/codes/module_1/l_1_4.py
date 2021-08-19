# -*- coding: utf-8 -*-

import numpy as np

a = np.mat(((1, 2), (5, 6)))
b = np.mat(((0, 1), (2, 3)))
print(a)
# Get matrix([[1, 2],
#               [5, 6]])
print(a + b)
# Get matrix([[1, 3],
#               [7, 9]])

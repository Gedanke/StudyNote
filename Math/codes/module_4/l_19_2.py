# -*- coding: utf-8 -*-

import math
import numpy as np
import random

x = np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1], [1, 0, 1]])
y = np.array([1, 0, 0, 0])
# y = np.array([0,0,1,1])
w = np.array([0.5, 0.5, 0.5])
a = 0.01
maxloop = 10000
for _ in range(maxloop):
    m = random.randint(0, 3)
    fi = 1.0 / (1 + math.pow(math.e, -np.dot(x[m], w)))
    g = (y[m] - fi) * x[m]
    w = w + a * g
    print(w)

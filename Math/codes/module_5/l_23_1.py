# -*- coding: utf-8 -*-

import random
import numpy as np

t = 0
f = 0
for i in range(1000):
    a = np.random.random((100, 1))
    all_max = max(a)
    get = 0
    m_max = max(a[0:37])
    for k in range(37, 100):
        if a[k] > m_max:
            get = a[k]
            break
    if get == all_max:
        t += 1
    else:
        f += 1
print("true: " + str(t))
print("false: " + str(f))
print("percentage: " + str(100.0 * t / (t + f)))

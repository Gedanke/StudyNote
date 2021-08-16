# -*- coding: utf-8 -*-

import random
import numpy as np

xbarlist = []
for i in range(1000):
    xbar = 0
    for j in range(30):
        k = random.randint(1, 6)
        xbar += k
    xbar = xbar / 30.0
    xbarlist.append(xbar)
npxbar = np.array(xbarlist)
mu = np.mean(npxbar)
var = np.var(npxbar)
print(mu)
print(var)

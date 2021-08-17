# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import math

x = list(range(1, 31, 1))
y1 = x
y2 = [pow(2, _) for _ in x]
y3 = [math.log2(_) for _ in x]

plot(x, y1, x, y2, x, y3)
x_mj = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_mj)
ax.yaxis.set_major_locator(x_mj)
plt.xlim(1, 30)
plt.ylim(0, 29)
plt.grid()
plt.savefig("../../images/module_3/16_9.png")
plt.show()

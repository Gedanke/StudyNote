# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import math

x = list(range(-10, 10, 1))
y = [1 / (1 + math.exp(-x_)) for x_ in x]

plot(x, y)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("sigmoid function")
plt.grid()
plt.savefig("../../images/module_4/19_9.png")
plt.show()

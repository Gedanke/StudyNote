# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from numpy import random

samples = random.rand(30, 2)
plt.scatter(samples[:, 1], samples[:, 0], color='green')
new_ticks = np.linspace(-1, 1, 5)
plt.xticks(new_ticks)
plt.yticks(new_ticks)
plt.savefig('../../images/module_2/12_1.png')
plt.close()
samples_a = samples - np.mean(samples, axis=0)
plt.scatter(samples_a[:, 1], samples_a[:, 0], color='red')
new_ticks = np.linspace(-1, 1, 5)
plt.xticks(new_ticks)
plt.yticks(new_ticks)
plt.savefig('../../images/module_2/12_2.png')
plt.close()

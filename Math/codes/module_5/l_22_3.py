# -*- coding: utf-8 -*-

import random
import math

inCircle = 0
distance = 0.0
for _ in range(1000):
    x = 1.0 * random.randint(0, 1000) / 100
    y = 1.0 * random.randint(0, 1000) / 100
    if x * x + y * y > 100:
        continue
    else:
        inCircle += 1
        distance += math.sqrt(x * x + y * y)
print(distance / inCircle)

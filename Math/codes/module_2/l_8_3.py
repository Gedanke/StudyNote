# -*- coding: utf-8 -*-

import random

fenzi = 0
fenmu = 0
for _ in range(1000):
    # 0 is girl; 1 is boy
    first = random.randint(0, 1)
    second = random.randint(0, 1)
    if first == 1 and second == 1:
        continue
    else:
        fenmu += 1
        if first == second:
            fenzi += 1

print(1.0 * fenzi / fenmu)

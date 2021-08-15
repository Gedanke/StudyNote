# -*- coding: utf-8 -*-

import random

obj = 0.0
for _ in range(10000):
    you = random.randint(1, 6)
    damihu = random.randint(1, 6)
    if damihu == 4 and you > damihu:
        obj += 1
        
print(obj / 10000)

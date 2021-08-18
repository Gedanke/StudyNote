# -*- coding: utf-8 -*-

import random

dapiaoliang = 0
you = 0
win = 0
for _ in range(1000):
    for _ in range(51):
        if random.randint(0, 1) == 1:
            dapiaoliang += 1
    for _ in range(50):
        if random.randint(0, 1) == 1:
            you += 1
    if dapiaoliang > you:
        win += 1
    dapiaoliang = 0
    you = 0
print(win)

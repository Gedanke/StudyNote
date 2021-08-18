# -*- coding: utf-8 -*-

import math


def sigmoid(x):
    if x < 0:
        y = math.pow(math.e, x) / (1 + math.pow(math.e, x))
    else:
        y = 1 / (1 + math.pow(math.e, -x))
    return y


a = -1000000
b = 1000000
print(sigmoid(a))
print(sigmoid(b))

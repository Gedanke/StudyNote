# -*- coding: utf-8 -*-

import math


def entropy(*c):
    result = 0
    islegal = 0
    for x in c:
        islegal += x
        result = result + (-x) * math.log(x, 2)
    if islegal != 1:
        return 'input prob error!'
    return result


if __name__ == '__main__':
    print(entropy(0.9, 0.1))
    print(entropy(0.4, 0.6))
    print(entropy(0.75, 0.25))

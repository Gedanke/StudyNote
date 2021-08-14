# -*- coding: utf-8 -*-

import math


def getSubsidy(k, b, m, c):
    rx = [-k, k * (m - c) - b, b * (m - c)]
    rpx = [-2 * k, k * (m - c) - b]
    return -rpx[1] / rpx[0]


def grad(x):
    fenzi1 = (-1 + 9 * math.exp(-x) - x * math.exp(-x)) * (1 + math.exp(-x))
    fenzi2 = -(8 - x) * (1 - math.exp(-x)) * math.exp(-x)
    fenmu = math.pow(1 + math.exp(-x), 2)
    return (fenzi1 - fenzi2) / fenmu


def main():
    a = 0.01
    maxloop = 1000
    xtemp = 0.1
    for _ in range(maxloop):
        g = grad(xtemp)
        if g < 0.00005:
            break
        xtemp = xtemp + a * g
    print(xtemp)


if __name__ == '__main__':
    main()

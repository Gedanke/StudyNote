# -*- coding: utf-8 -*-
import math


def grad(x):
    return (5 - 6 * x) / (x * (1 - x))


def main():
    a = 0.01
    maxloop = 1000
    theta = 0.1
    for _ in range(maxloop):
        g = grad(theta)
        theta = theta + a * g
    print(theta)


if __name__ == '__main__':
    main()

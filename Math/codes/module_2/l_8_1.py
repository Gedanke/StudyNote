# -*- coding: utf-8 -*-

import random


def main():
    m = 0
    n = 1000
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y < 1:
            m += 1
    print(1.0 * m / n)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-

def hanoi(N, x, y, z):
    if N == 1:
        print(x + '->' + z)
    else:
        hanoi(N - 1, x, z, y)
        print(x + '->' + z)
        hanoi(N - 1, y, x, z)


hanoi(3, 'a', 'b', 'c')

# -*- coding: utf-8 -*-


def binary_search(obj, a, begin, end):
    median = int((begin + end) / 2)
    if obj == a[median]:
        print(median)
    elif begin > end:
        print(-1)
    else:
        if obj > a[median]:
            binary_search(obj, a, median + 1, end)
        else:
            binary_search(obj, a, begin, median - 1)


a = [1, 2, 7, 11, 14, 24, 33, 37, 44, 51]
binary_search(7, a, 0, 9)

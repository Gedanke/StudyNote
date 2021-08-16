# -*- coding: utf-8 -*-

def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n - 1)

# -*- coding: utf-8 -*-

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        print("fib: " + str(n - 1))
        print("fib: " + str(n - 2))
        return fib(n - 1) + fib(n - 2)


fib(10)

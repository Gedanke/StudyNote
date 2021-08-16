# -*- coding: utf-8 -*-

import sys

n = int(sys.argv[1])
result = 0
for i in range(n + 1):
    if i % 2 == 0:
        result += i
print(result)

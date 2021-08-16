# -*- coding: utf-8 -*-

import time
import sys

t1 = int(time.time() * 1000000)
n = int(sys.argv[1])
result = 0
for i in range(n):
    result += i
t2 = int(time.time() * 1000000)
print(t2 - t1)

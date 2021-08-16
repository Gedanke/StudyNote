# -*- coding: utf-8 -*-

import random

exp = []
con = []
for i in range(1000):
    value = random.randint(1, 100)
    if value <= 30:
        exp.append(i)
    else:
        con.append(i)

print(len(exp))
print(len(con))

# -*- coding: utf-8 -*-

left = 0
left_temp = 0
right = 0
for k in range(1, 100):
    left_temp = 2 * k - 1
    left += left_temp
    right = k * k
    if left == right:
        print(str(k) + " is right!")

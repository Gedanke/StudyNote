# -*- coding: utf-8 -*-

a = [1, 2, 2, 3, 4, 5]
index_max = 0
times_max = -1
for i in range(len(a)):
    times_temp = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            times_temp += 1
    if times_temp > times_max:
        times_max = times_temp
        index_max = i
result = a[index_max]
for k in range(len(a)):
    result += a[k]
print(result)

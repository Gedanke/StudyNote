# -*- coding: utf-8 -*-

a = [2, 1, 4, 3, 4, 2, 3]
for i in range(0, len(a)):
    times = 0
    for j in range(0, len(a)):
        if a[i] == a[j]:
            times += 1
    if times == 1:
        print(a[i])
        break

a = [2, 1, 4, 3, 4, 2, 3]
result = a[0]
for i in range(1, len(a)):
    result = result ^ a[i]
print(result)

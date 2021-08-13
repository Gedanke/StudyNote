# -*- coding: utf-8 -*-

a = 8
b = str(bin(a))
total = 0
for i in range(2, len(b)):
    total += int(b[i])
if total == 1 and b[2] == '1':
    print('yes')
else:
    print('no')

# yes

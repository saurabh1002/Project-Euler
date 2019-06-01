# -*- coding: utf-8 -*-

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

for i in xrange (2, 1001):
    list = []
    rem = 1
    while 1:
        rem = rem % i
        if rem == 0:
            break
        if rem in list:
            count = len(list) - list.index(rem)
            print (i, count)
            break
        list.append(rem)
        rem = rem * 10


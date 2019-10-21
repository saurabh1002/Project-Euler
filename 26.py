# -*- coding: utf-8 -*-

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from common_functions import timing

timer = timing()

largest_count = 0
d = 0
for i in range (2, 1000):
    list = []
    rem = 1
    while 1:
        rem = rem % i
        if rem == 0:
            break
        if rem in list:
            count = len(list) - list.index(rem)
            if count > largest_count:
                largest_count = count
                d = i
            break
        list.append(rem)
        rem = rem * 10

timer("The value of d < 1000 for which 1/d contains the longest recurring cycle is {}".format(d))

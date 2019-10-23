# -*- coding: utf-8 -*-

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import copy
from common_functions import timing

timer = timing()
list = ['8', '7', '6', '5', '4', '3', '2']
pan = []
sum = 0
a = '9'
i = '1'

for b in list:
    list_b = copy.copy(list)
    list_b.remove(b)
    for c in list_b:
        list_c = copy.copy(list_b)
        list_c.remove(c)
        for d in list_c:
            list_d = copy.copy(list_c)
            list_d.remove(d)
            for e in list_d:
                list_e = copy.copy(list_d)
                list_e.remove(e)
                for f in list_e:
                    list_f = copy.copy(list_e)
                    list_f.remove(f)
                    for g in list_f:
                        list_g = copy.copy(list_f)
                        list_g.remove(g)
                        for h in list_g:
                            list_h = copy.copy(list_g)
                            list_h.remove(h)
                            if (int(a + b + c + d) * 2) == int(i + e + f + g + h):
                                timer("The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1 is {}".format(
                                    int(a + b + c + d + i + e + f + g + h)))
                                break

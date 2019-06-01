# -*- coding: utf-8 -*-

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import copy

list = ['8', '7', '6', '5', '4', '3', '2']
pan = []
sum = 0
a = '9'
i = '1'

for b in list:
    list_b = copy.copy(list)
    list_b.remove(b)
    # print b
    for c in list_b:
        list_c = copy.copy(list_b)
        list_c.remove(c)
        # print c
        for d in list_c:
            list_d = copy.copy(list_c)
            list_d.remove(d)
            # print d
            for e in list_d:
                list_e = copy.copy(list_d)
                list_e.remove(e)
                # print e
                for f in list_e:
                    list_f = copy.copy(list_e)
                    list_f.remove(f)
                    # print f
                    for g in list_f:
                        list_g = copy.copy(list_f)
                        list_g.remove(g)
                        # print g
                        for h in list_g:
                            list_h = copy.copy(list_g)
                            list_h.remove(h)
                            # print h
                            if (int(a + b + c + d) * 2) == int(i + e + f + g + h):
                                print (int(a + b + c + d + i + e + f + g + h))
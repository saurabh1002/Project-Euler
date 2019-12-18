# -*- coding: utf-8 -*-

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

                            # d2d3d4=406 is divisible by 2
                            # d3d4d5=063 is divisible by 3
                            # d4d5d6=635 is divisible by 5
                            # d5d6d7=357 is divisible by 7
                            # d6d7d8=572 is divisible by 11
                            # d7d8d9=728 is divisible by 13
                            # d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

import copy
from common_functions import timing

timer = timing()

list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pan_num = []
for a in list[1:10]:
    list_a = copy.copy(list)
    list_a.remove(a)
    for b in list_a:
        list_b = copy.copy(list_a)
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
                                for i in list_h:
                                    list_i = copy.copy(list_h)
                                    list_i.remove(i)
                                    for j in list_i:
                                        if ((int(h + i + j)% 17) == 0):
                                            if ((int(g + h + i)% 13) == 0):
                                                if ((int(f + g + h)% 11) == 0):
                                                    if ((int(e + f + g)% 7) == 0):
                                                        if ((int(d + e + f)% 5) == 0):
                                                            if ((int(c + d + e)% 3) == 0):
                                                                if ((int(b + c + d)% 2) == 0):
                                                                    pan_num.append(int(a + b + c + d + e + f + g + h + i + j))
sum = 0
for i in pan_num:
    sum = sum + i

timer("Sum of all 0 to 9 pandigital numbers with the given property is {}".format(sum))
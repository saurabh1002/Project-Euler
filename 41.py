# -*- coding: utf-8 -*-

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import copy
from math import *
from common_functions import check_prime, timing

timer = timing()

list = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
pan_prime = []
while(len(pan_prime) == 0):
    for a in list:
        list_a = copy.copy(list)
        list_a.remove(a)
        if(len(list_a) != 0):
            for b in list_a:
                list_b = copy.copy(list_a)
                list_b.remove(b)
                if(len(list_b) != 0):
                    for c in list_b:
                        list_c = copy.copy(list_b)
                        list_c.remove(c)
                        if(len(list_c) != 0):
                            for d in list_c:
                                list_d = copy.copy(list_c)
                                list_d.remove(d)
                                if(len(list_d) != 0):
                                    for e in list_d:
                                        list_e = copy.copy(list_d)
                                        list_e.remove(e)
                                        if(len(list_e) != 0):
                                            for f in list_e:
                                                list_f = copy.copy(list_e)
                                                list_f.remove(f)
                                                if(len(list_f) != 0):
                                                    for g in list_f:
                                                        list_g = copy.copy(list_f)
                                                        list_g.remove(g)
                                                        if(len(list_g) != 0):
                                                            for h in list_g:
                                                                list_h = copy.copy(list_g)
                                                                list_h.remove(h)
                                                                if(len(list_h) != 0):
                                                                    for i in list_h:
                                                                        if (check_prime(int(a + b + c + d + e + f + g + h + i))):
                                                                            pan_prime.append(int(a + b + c + d + e + f + g + h + i))
                                                                else:
                                                                    if (check_prime(int(a + b + c + d + e + f + g + h))):
                                                                        pan_prime.append(int(a + b + c + d + e + f + g + h))
                                                        else:
                                                            print (int(a + b + c + d + e + f + g))
                                                            temp = check_prime(int(a + b + c + d + e + f + g))
                                                            if (temp == 1):
                                                                pan_prime.append(int(a + b + c + d + e + f + g))
                                                else:
                                                    if (check_prime(int(a + b + c + d + e + f))):
                                                        pan_prime.append(int(a + b + c + d + e + f))
                                        else:
                                            if (check_prime(int(a + b + c + d + e))):
                                                pan_prime.append(int(a + b + c + d + e))
                                else:
                                    if (check_prime(int(a + b + c + d))):
                                        pan_prime.append(int(a + b + c + d))
                        else:
                            if (check_prime(int(a + b + c))):
                                pan_prime.append(int(a + b + c))
                else:
                    if (check_prime(int(a + b))):
                        pan_prime.append(int(a + b))
        else:
            if (check_prime(int(a))):
                pan_prime.append(int(a))
    list.pop(0)

timer("The largest n digit pandigital prime is {}".format(pan_prime[0]))

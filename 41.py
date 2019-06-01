# -*- coding: utf-8 -*-

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import copy
from math import *

def check_prime(number):
    if (number == 1):
        return False
    if (number == 2 or number == 3):
        return True
    i = 2
    while (i <= sqrt(number)):
        if(number % i == 0):
            return False
        i = i + 1
    return True

list = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]
pan_prime = []
while(len(pan_prime) == 0):
    for a in list:
        print (a,list)
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
                                                                            print('9', list)
                                                                            pan_prime.append(int(a + b + c + d + e + f + g + h + i))
                                                                else:
                                                                    if (check_prime(int(a + b + c + d + e + f + g + h))):
                                                                        print('8', list)
                                                                        pan_prime.append(int(a + b + c + d + e + f + g + h))
                                                        else:
                                                            print (int(a + b + c + d + e + f + g))
                                                            temp = check_prime(int(a + b + c + d + e + f + g))
                                                            if (temp == 1):
                                                                print('7', list)
                                                                pan_prime.append(int(a + b + c + d + e + f + g))
                                                else:
                                                    if (check_prime(int(a + b + c + d + e + f))):
                                                        print('6')
                                                        pan_prime.append(int(a + b + c + d + e + f))
                                        else:
                                            if (check_prime(int(a + b + c + d + e))):
                                                print('5')
                                                pan_prime.append(int(a + b + c + d + e))
                                else:
                                    if (check_prime(int(a + b + c + d))):
                                        print('4')
                                        pan_prime.append(int(a + b + c + d))
                        else:
                            if (check_prime(int(a + b + c))):
                                print('3')
                                pan_prime.append(int(a + b + c))
                else:
                    if (check_prime(int(a + b))):
                        print ('2')
                        pan_prime.append(int(a + b))
        else:
            if (check_prime(int(a))):
                print ('1')
                pan_prime.append(int(a))
    list.pop(0)
    print(list)
print (pan_prime[0])

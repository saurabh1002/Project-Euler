# -*- coding: utf-8 -*-

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?


from math import *
import copy

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

def get_sorted_digits(number):
    list = []
    while number != 0:
        list.append(str(number % 10))
        number = (number - (number % 10)) / 10
    list.sort(key = int)
    return list

for i in xrange (1001, 10000, 2):
    if (check_prime(i) == 1):
        j = i
        list_a = get_sorted_digits(j)
        for a in list_a:
            list_b = copy.copy(list_a)
            list_b.remove(a)
            # print b
            for b in list_b:
                list_c = copy.copy(list_b)
                list_c.remove(b)
                # print c
                for c in list_c:
                    list_d = copy.copy(list_c)
                    list_d.remove(c)
                    # print d
                    for d in list_d:
                        num = int (a + b + c + d)
                        if num > i:
                            if (check_prime(num) == 1):
                                diff = num - i
                                if (check_prime(num + diff) == 1):
                                    list_new = get_sorted_digits(num + diff)
                                    if list_new == list_a:
                                        print (i, num, (num + diff))



# -*- coding: utf-8 -*-

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import *

ddef check_prime(number):
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

flag = True
odd_comp = 35
while (flag != False):
    if ((check_prime(odd_comp)) == False):
        GoldBach = False
        for i in xrange (3, odd_comp, 2):
            if (check_prime(i)):
                if (sqrt((odd_comp - i) / 2) == int(sqrt((odd_comp - i) / 2))):
                    print odd_comp, i
                    GoldBach = True
        if (GoldBach != True):
            flag = False
            print odd_comp
    odd_comp = odd_comp + 2
    print odd_comp

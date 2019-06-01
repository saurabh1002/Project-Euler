# -*- coding: utf-8 -*-

# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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

def distinct_factors(num):
    if check_prime(num):
        return 1
    number = copy.copy(num)
    i = 3
    count = 0

    if number % 2 == 0:
        while number % 2 == 0:
            number = number / 2
        count  = 1

    while (count <= 4 and number != 1):
        if number % i == 0:
            if check_prime(i):
                count = count + 1
                while number % i == 0:
                    number = number / i
        i = i + 2

    if count == 4:
        print count, num
    return count

i = 1000
while 1:
    a = distinct_factors(i + 3)
    if a == 4:
        b = distinct_factors(i + 2)
        if b == 4:
            c = distinct_factors(i + 1)
            if c == 4:
                d = distinct_factors(i)
                if d == 4:
                    print i
                    break
                else:
                    i = i + 1
            else:
                i = i + 2
        else:
            i = i + 3
    else:
        i = i + 4

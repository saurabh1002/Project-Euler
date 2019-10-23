# -*- coding: utf-8 -*-
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from math import *
from common_functions import timing, check_prime

def check_any_even_number(num):
    while (num != 0):
        if ((num % 2) == 0):
            return False
        else:
            num = (num - (num % 10)) / 10
    return True

def rotate_num(num):
    last_digit = num % 10
    num = (num - (last_digit)) / 10
    return (int(float(str(last_digit) + str(num))))

timer = timing()

count = 13
for i in range(101, 1000000, 2):
    if check_any_even_number(i):
        if (check_prime(i)):
            flag = 1
            l = len(str(i))
            for j in range (0, l):
                i = rotate_num(i)
                if (check_prime(i)):
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                count = count + 1

timer("There are {} circular primes below one million".format(count))

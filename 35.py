# -*- coding: utf-8 -*-
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

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

def check_even_number(num):
    while (num != 0):
        if (((num % 10) % 2) == 0):
            return False
        else:
            num = (num - (num % 10)) / 10
    return True

def rotate_num(num):
    last_digit = num % 10
    num = (num - (last_digit)) / 10
    return (int(str(last_digit) + str(num)))

count = 13
for i in xrange(101, 1000000, 2):
    if check_even_number(i):
        if (check_prime(i)):
            flag = 1
            l = len(str(i))
            for j in xrange (0, l):
                i = rotate_num(i)
                if (check_prime(i)):
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                count = count + 1

print count

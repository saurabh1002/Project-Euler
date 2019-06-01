# -*- coding: utf-8 -*-
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

def right_trunc(num):
    while num != 0:
        if check_prime(num):
            num = (num - (num % 10)) / 10
        else:
            return False
    return True

def left_trunc(num):
    i = 1
    temp = 0
    while(temp != num):
        temp = num % (10 ** i)
        if check_prime(temp):
            i = i + 1
        else:
            return False
    return True

num = 11
count = 0
sum = 0
while (count != 11):
    if right_trunc(num):
        if left_trunc(num):
            count = count + 1
            sum = sum + num

    num = num + 2
print sum
